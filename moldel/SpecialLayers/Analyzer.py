from collections import namedtuple
from Layer import Layer
from Learners import Learner, Predicter
from Learners.Learner import IO_Pair
import os
import pickle
import rootpath

Timed_Label = namedtuple("Timed_Label", ["label", "season", "episode"])
Linked_Predicter = namedtuple("Linked_Predicter", ["predicter", "train_seasons"])
Prediction = namedtuple("Prediction", ["timed_label", "prediction"])

class Analyzer(Layer):
    """ An Analyzer will compute a likelihood distribution by using 'labels'. It will first check and learn from how
    these types of 'labels' were classified during the train seasons. Secondly after learning it will predict how these
    labels will be classified during the predict season. And the last step is that using these predictions it determines
    a likelihood distribution for the predict season. """

    __PREDICTER_STORE_FOLDER = "/moldel/Data/ExamData/Results/"

    def __init__(self, learner: Learner, name: str, store_mode: bool, store_folder: str):
        """ Constructor of Analyzer.

        Parameters:
            learner (Learner): The algorithm used to learn the pattern in the data.
        """
        self.learner = learner
        self.name = name
        self.store_mode = store_mode
        self.store_folder = store_folder

    def compute_distribution(self, predict_season: int, latest_episode: int, train_seasons: set) -> dict:
        all_labels = self._get_all_labels()
        predicter = self._train(all_labels, train_seasons)
        predictions = self._predict(predict_season, latest_episode, all_labels, predicter)
        return self.predictions_to_distribution(predictions)

    def _train(self, all_labels: list, train_seasons: set) -> Predicter:
        if self.store_mode:
            predicter = self._load_predicter(train_seasons)
            if not predicter is None:
                return predicter

        train_data = []
        for timed_label in all_labels:
            if timed_label.season in train_seasons:
                train_data.append(IO_Pair(self._label_to_input(timed_label), self._label_to_output(timed_label)))
        predicter = self.learner.train()

        if self.store_mode:
            self._save_predicter(predicter, train_seasons)

        return predicter

    def _predict(self, predict_season: int, latest_episode: int, all_labels: list, predicter: Predicter) -> list:
        predictions = []
        for timed_label in all_labels:
            if timed_label.season == predict_season and timed_label.episode <= latest_episode:
                predictions.append(Prediction(timed_label, predicter.predict(self._label_to_input(timed_label))))
        return predictions

    def _load_predicter(self, train_seasons: set) -> Predicter:
        store_path = rootpath.detect() + self.store_folder
        for filename in os.listdir(store_path):
            if filename.startswith(self.name):
                linked_predicter = pickle.load(filename)
                if linked_predicter.train_seasons == train_seasons:
                    return linked_predicter.predicter
        return None

    def _save_predicter(self, predicter: Predicter, train_seasons: set):
        store_path = rootpath.detect() + self.store_folder
        max_file_index = 0
        for filename in os.listdir(store_path):
            filename_split = filename.split(self.name)
            if len(filename_split) > 1:
                max_file_index = max(max_file_index, int(filename_split[1]))
        linked_predicter = Linked_Predicter(predicter, train_seasons)
        store_file = store_path + self.name + str(max_file_index + 1)
        pickle.dump(linked_predicter, store_file)

    def _get_all_labels(self) -> list:
        pass

    def predictions_to_distribution(self, predictions: list) -> dict:
        pass

    def _label_to_input(self, timed_label):
        pass

    def _label_to_output(self, timed_label):
        pass


from DistributionTransformers.NormalizeTransformer import NormalizeTransformer
from Layer import Layer
from WikiWordLayer.DataExtractors.Output_Extractor import Output_Extractor
from WikiWordLayer.DataParsers.DataParser import DataParser
from WikiWordLayer.DataSelectors.Normal_Train_Selector import Normal_Train_Selector
from WikiWordLayer.DataSelectors.Predict_Selector import Predict_Selector
from WikiWordLayer.DataSelectors.Strict_Train_Selector import Strict_Train_Selector

class WikiWordLayer(Layer):
    """ The Wiki Word Layer predicts which candidate is the Mol based on their wikipedia pages. """

    def __init__(self, input_extractor, predicter, strict):
        """ Create a Wiki Word Layer.
        Arguments:
            input_extractor: The Data Extractor class used to convert the candidates to numberic vectors
            predicter: The Data Predictor class used to determine how likely numberic vectors are the Mol based
            on the numberic vectors used for training
            strict (bool): If true then only seasons before the predict season will be used as training data. If false
            then all seasons are used as training data except the season for which we predict the result.
        """
        self.input_extractor = input_extractor
        self.predicter = predicter
        if strict:
            self.train_selector = Strict_Train_Selector()
        else:
            self.train_selector = Normal_Train_Selector()

    def compute_distribution(self, season, episode):
        parsed_data = DataParser.parse()
        numberic_input = self.input_extractor.extract(parsed_data)
        numberic_output = Output_Extractor().extract(parsed_data)
        train_input = self.train_selector.select(numberic_input, parsed_data, season)
        train_output = self.train_selector.select(numberic_output, parsed_data, season)
        self.predicter.train(train_input, train_output)
        predict_input = Predict_Selector().select(numberic_input, parsed_data, season)
        predict_output = self.predicter.predict(predict_input)
        normalizer = NormalizeTransformer()
        return normalizer.transform_distribution(predict_output)
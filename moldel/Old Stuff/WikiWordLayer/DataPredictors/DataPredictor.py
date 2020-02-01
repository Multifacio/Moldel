class DataPredictor:
    """ The Data Predictor will be trained on the numberic train data (both input/output) and after that will predict
    who is likely to be the Mol based on the numberic input predict data. """

    def train(self, train_input, train_output):
        """ Train the Data Predictor instance with training data. (You should only execute this once)
        Arguments:
            train_input (dict): The numberic data used as training input, more information can be found in
            DataExtractor (same data type as return value).
            train_output (dict): The numberic data used as training output, more information can be found in
            DataExtractor (same data type as return value). """
        pass

    def predict(self, predict_input):
        """ Predict which candidate is the Mol. (You should only execute this after you execute train)
        Arguments:
            predict_input (dict): The numberic data for which we want to predict whether that candidate is the Mol,
            more information can be found in DataExtractor (same data type as return value).
        Returns:
            A dictionary with as keys the candidates and as values non-negative floats which are higher if the
            candidate is more likely to be the Mol. """
        pass
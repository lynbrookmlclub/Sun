"""
Base class for supervised learning.
"""


class Algorithm():
    """
    Inherit and implement __init__, fit, predict, and evaluate.
    """

    def __init__(self) -> None:
        """
        Takes in whatever parameters are needed.
        """

    def fit(self, X_train, y_train):
        """
        This is where the model should be trained based on the data.
        """
        raise NotImplementedError

    def predict(self, X_test): 
        """
        Give predicted output from input.
        """
        raise NotImplementedError

    def evaluate(self, X_test, y_test): 
        """
        Evaluate how good the predictions are.
        """
        raise NotImplementedError

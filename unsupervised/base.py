"""
Base class for unsupervised learning.
"""


class Algorithm():
    """
    Not the same as supervised/base.py/Algorithm
    You can also add evaluate()
    """

    def __init__(self) -> None:
        """
        Take arguments here.
        """

    def fit_predict(self, X_train): 
        """
        Generates labels.
        Never take labels in unsupervised learning.
        """
        raise NotImplementedError()

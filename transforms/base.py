"""
Base class for transformations.
"""


class Preprocesser():
    # we didn't want to call this a transformer because that's something else...

    def __init__(self) -> None:
        """
        Take arguments here.
        """

    def fit(self, X):
        """
        Fit method for the preprocesser.
        Will use learned info in the transformation (e.g. the mean in normalization) 
        """
        raise NotImplementedError
    
    def fit_transform(self, X): 
        """
        This will learn on the data and transform X based on it.
        """
        raise NotImplementedError

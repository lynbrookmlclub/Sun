# contains the base class. 

class Algorithm():
    # DO NOT confuse this with the Algorithm() class from supervised/base.py
    def __init__(self) -> None:
        # takes in whatever parameters are needed
        pass
    def fit_predict(self, X_train): 
        # in unsupervised learning, you never take labels (you make the labels)
        raise NotImplementedError()

    # some unsupervised algorithms also have an evaluate() method 
    # so you can add that too. 

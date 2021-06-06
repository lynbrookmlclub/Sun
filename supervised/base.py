# contains the base class. 

class Algorithm():
    def __init__(self) -> None:
        # takes in whatever parameters are needed
        pass
    def fit(self, X_train, y_train):
        # this is where the model should be trained based on this data 
        raise NotImplementedError

    def predict(self, X_test): 
        # here you should use what was learnt to make predictions about X_test
        raise NotImplementedError
    def evaluate(self, X_test, y_test): 
        # this is where the model's predictions should be evaluated 
        raise NotImplementedError

# In short, the __init__(), fit(), predict(), and evaluate() method all need to be written. 
# this contains the base classes for all transformations


class Preprocesser(): 
    # we didn't want to call this a transformer because that's something else...

    def __init__(self) -> None:
        
        # save any arguments here   
        pass 
    
    def fit(self, X):
        # here is the fit method just for the preprocesser 
        # to learn some information it will use in the transformation (e.g. the mean in normalization) 

        raise NotImplementedError
    
    def fit_transform(self, X): 
        # this will learn on the data 
        # and then transform X based on it 
        raise NotImplementedError
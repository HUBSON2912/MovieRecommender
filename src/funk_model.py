import numpy as np

class Funk:
    def __init__(self, nusers:int, nitems:int, secdim:int, regulation_param:float):
        self.P:np.matrix = np.random.random((nusers,secdim))
        self.Q:np.matrix = np.random.random((secdim,nitems))
        self.regparam:float=regulation_param

    def __lossFunction(self):
        raise NotImplemented()

    def __derivativeP(self):
        raise NotImplemented()

    def __derivativeQ(self):
        raise NotImplemented()

    def __updateMatrix(self):
        raise NotImplemented()

    def train(self, ratings:dict[tuple[int,int], float]):
        raise NotImplemented()

    def predict(self, user:int, item:int) -> float:
        raise NotImplemented()
    
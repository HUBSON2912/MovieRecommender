import numpy as np
import copy

class Funk:
    def __init__(self, nusers:int, nitems:int, secdim:int, regulation_param:float, learn_rate:float, learn_rate_decay=0.05):
        self.nusers:int = nusers
        self.nitems:int = nitems
        self.secdim:int = secdim
        self.learning_rate:float=learn_rate

        self.__regulationParam:float=regulation_param
        self.__initialLearningRate:float=learn_rate
        self.__learningRateDecay=learn_rate_decay

        self.__P:np.ndarray[np.ndarray[float]] = np.random.rand(nusers,secdim)
        self.__Q:np.ndarray[np.ndarray[float]] = np.random.rand(secdim,nitems)

    def __predictionError(self, user, item): 
        return self.trainData[user,item] - self.predict(user, item)

    
    def lossFunction(self):  # mean square error
        sum=0
        keys:list[tuple[int,int]]=self.trainData.keys()
        for key in keys:
            sum+=self.__predictionError(key[0],key[1])**2
        
        return sum/len(keys)

    def __derivativeP(self, user) -> np.ndarray:
        sum:np.ndarray = np.zeros((self.secdim,))
        _QTransp=self.__Q.transpose()
        for key in self.trainData.keys():
            _,i=key
            try:
                sum+=-2 * (self.trainData[(user,i)] - np.dot(self.__P[user], _QTransp[i])) * (_QTransp[i])
            except KeyError:
                # skip not rated
                # does it ever happen?
                continue

        sum=sum/self.nitems
        sum+=2*self.__regulationParam*self.__P[user]

        return sum

    def __derivativeQ(self, item) -> np.ndarray:
        sum:np.ndarray = np.zeros((self.secdim,))
        _QTransp=self.__Q.transpose()
        for key in self.trainData.keys():
            u,_=key
            try:
                sum+=-2 * (self.trainData[(u,item)] - np.dot(self.__P[u], _QTransp[item])) * (self.__P[u])
            except KeyError:
                # skip not rated
                continue

        sum=sum/self.nusers
        sum+=2*self.__regulationParam*_QTransp[item]

        return sum

    def __updateMatrix(self, iternum=None):
        _QTransp:np.ndarray = copy.deepcopy(self.__Q)
        _QTransp=_QTransp.transpose()
        _counterPercent:int=0
        _keys=self.trainData.keys()

        for u,i in _keys:
            _counterPercent+=1
            pu_row=copy.deepcopy(self.__P[u])
            qi_column = copy.deepcopy(_QTransp[i])

            # update
            self.__P[u]=pu_row - (self.learning_rate * self.__derivativeP(u)) * qi_column  - self.learning_rate * self.__regulationParam * pu_row
            _QTransp[i]=qi_column - pu_row * (self.__derivativeQ(i) * self.learning_rate) - self.learning_rate * self.__regulationParam * qi_column

            # progress info
            if int(100*(_counterPercent-1)/len(_keys)) != int(100*_counterPercent/len(_keys)):
                print(f"Iter: {iternum}\tProgress: {_counterPercent} / {len(_keys)} = {int(100*_counterPercent/len(_keys))}")
            
        self.__Q=_QTransp.transpose()

    def train(self, ratings:dict[tuple[int,int], float], max_iterations=100, error_tolerance=1e-3):
        self.trainData=ratings
        for i in range(max_iterations):
            self.__updateMatrix(i+1)
            error = self.lossFunction()

            self.learning_rate = self.__initialLearningRate/(1+i*self.__learningRateDecay)

            print(f"===========================\nIteration {i+1} finished\nError = {error}\n===========================")
            if error<error_tolerance:
                print("Error tolerance reached")
                break

    def predict(self, user:int, item:int) -> float:
        return np.dot(self.__P[user], self.__Q.transpose()[item])

    def printPredictions(self):
        for u in range(self.nusers):
            print(f"{u}: ",end="")
            for i in range(self.nitems):
                print(self.predict(u,i), end=";")
            print()
    
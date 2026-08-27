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
                sum += -2 * (self.__predictionError(user, i)) * _QTransp[i]
            except KeyError:
                # skip not rated
                # does it ever happen?
                continue
        
        sum += 2*self.__regulationParam*self.__P[user]

        return sum

    def __derivativeQ(self, item) -> np.ndarray:
        sum:np.ndarray = np.zeros((self.secdim,))

        for key in self.trainData.keys():
            u,_=key
            try:
                sum += -2 * self.__predictionError(u, item) * self.__P[u]
            except KeyError:
                # skip not rated
                continue

        sum+=2*self.__regulationParam*self.__Q.transpose()[item]

        return sum

    def __updateMatrix(self, iternum=None):
        _PCPY:np.ndarray=copy.deepcopy(self.__P)
        _QTranspCPY:np.ndarray = copy.deepcopy(self.__Q)
        _QTranspCPY=_QTranspCPY.transpose()

        _counterPercent:int=0
        _keys=self.trainData.keys()

        for u,i in _keys:
            _counterPercent+=1
            pu_row=copy.deepcopy(_PCPY[u])
            qi_column = copy.deepcopy(_QTranspCPY[i])

            # update
            _PCPY[u] = pu_row - self.learning_rate * self.__derivativeP(u)
            _QTranspCPY[i] = qi_column - self.learning_rate * self.__derivativeQ(i)


            # progress info
            if int(100*(_counterPercent-1)/len(_keys)) != int(100*_counterPercent/len(_keys)):
                print(f"Iter: {iternum}\tProgress: {_counterPercent} / {len(_keys)} = {int(100*_counterPercent/len(_keys))}")

        self.__P=_PCPY
        self.__Q=_QTranspCPY.transpose()

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
        print(np.matmul(self.__P, self.__Q))
    
from __future__ import annotations
import pickle
import numpy as np
import matplotlib.pyplot as plt
import copy
import datetime
import consts
from pathlib import Path
from typing import Optional

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
        self.__errors:list[float]=[]

    @staticmethod
    def getDummy():
        return Funk(1,1,1,1,1,1)

    def __predictionError(self, user, item): 
        return self.trainData[user,item] - self.predict(user, item)
   
    def lossFunction(self):
        sum=0
        keys:list[tuple[int,int]]=self.trainData.keys()
        for key in keys:
            sum+=self.__predictionError(key[0],key[1])**2
        
        return sum/len(keys)

    def __updateMatrix(self, iternum=None):
        _counterPercent:int=0
        _keys=self.trainData.keys()

        for u,i in _keys:
            _counterPercent+=1

            error=self.__predictionError(u,i)
            pu_row=copy.deepcopy(self.__P[u])
            qi_col=copy.deepcopy(self.__Q[:, i])

            # update
            # earlier the derivatives were using the sum so if one 
            # user rated 100 movies and the other rated 5 it has an impact 
            # (error*vec) is a part of derivative so it's not bad
            self.__P[u] = pu_row + self.learning_rate*(error*qi_col - self.__regulationParam*pu_row)
            self.__Q[:,i] = qi_col + self.learning_rate*(error*pu_row - self.__regulationParam*qi_col)

            # progress info
            # every 10%
            if int(10*(_counterPercent-1)/len(_keys)) != int(10*_counterPercent/len(_keys)):
                print(f"Iter: {iternum}\tProgress: {_counterPercent} / {len(_keys)} = {int(100*_counterPercent/len(_keys))}")

    def train(self, ratings:dict[tuple[int,int], float], max_iterations=100, error_tolerance=1e-3):
        self.trainData=ratings
        for i in range(max_iterations):
            self.__updateMatrix(i+1)
            error = self.lossFunction()

            self.learning_rate = self.__initialLearningRate/(1+i*self.__learningRateDecay)
            self.__errors.append(error)

            print(f"===========================\nIteration {i+1} finished\nError = {error}\n===========================")
            if error<error_tolerance:
                print("Error tolerance reached")
                break

    def predict(self, user:int, item:int) -> float:
        return np.dot(self.__P[user], self.__Q.transpose()[item])

    def printPredictions(self):
        # error graph
        fig, ax = plt.subplots()
        x,y=list(range(len(self.__errors))), self.__errors
        ax.plot(x,y)
        ax.grid()
        ax.set(title="Error in each iteration")
        plt.show()

        # every prediction
        print("Predicions:\n")
        print(np.matmul(self.__P, self.__Q))

        # error for each input data
        print("Error for input:\n")
        for u,i in self.trainData.keys():
            Rp=self.predict(u,i)
            R=self.trainData[(u,i)]
            print(f"{(u,i)}:\tR={R}\tR'={Rp}\tdR={Rp-R}")

    def save(self, name:Optional[str]=None):
        savePath:Path=consts.SAVE_DIR
        if not (name is None):
            savePath=savePath / f"{name}.bin"
        else:
            now=datetime.datetime.now()
            savePath = savePath / f"funk-model-{now.year}-{now.month}-{now.day}T{now.hour}:{now.minute}:{now.second}.bin"

        with open(savePath, "wb") as saveFile:
            pickle.dump(self.__dict__, saveFile)

    @staticmethod
    def load(path:Path) -> Funk:
        if not path.exists():
            raise FileNotFoundError(f"File '{path}' doesn't exist")

        with open(path, "rb") as saved:
            tmpDict=pickle.load(saved)
            loaded=Funk.getDummy() # dump values
            loaded.__dict__.clear()
            loaded.__dict__.update(tmpDict)
            return loaded
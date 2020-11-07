import math

import sys

class Matrix():

    def __init__(self,N=4):
        self.N = N
        self.container = [[0 for _ in range(self.N)] for _ in range(self.N)]

    def __getitem__(self,key):
        return self.container[key]
    def __setitem__(self,key, value):
        self.container[key] = value

    def __str__(self):
        matrixtostring=""
        for i in range(self.N):
            matrixtostring += " ".join([str(s) for s in self.container[i]]) + "\n"
            
        return matrixtostring

    def __eq__(self,other):
        if(not(self.N == other.N)):
            raise AttributeError("Matrices must have the same number of colums")
        return all([math.isclose(self.container[i][j],other.container[i][j]) for i in range(self.N) for j in range(self.N)])



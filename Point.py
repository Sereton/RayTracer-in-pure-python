from  BasicTuple import *

from Vector import Vector
class Point(BasicTuple):
    def __init__(self,x,y,z):
        self.w=1
        super(Point,self).__init__(x,y,z,self.w)

    def __sub__(self,other):
        
        x= self.x - other.x
        y= self.y - other.y
        z= self.z - other.z
        
        if other.w == 0:
            return self.__class__(x,y,z)
        else:
            return Vector(x,y,z)
        
        

        



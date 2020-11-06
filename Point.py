from  BasicTuple import *
class Point(BasicTuple):
    def __init__(self,x,y,z):
        self.w=1
        super(Point,self).__init__(x,y,z,self.w)
        

s = Point(1,2,3)
print(s.x)



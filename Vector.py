from  BasicTuple import BasicTuple
class Vector(BasicTuple):
    def __init__(self,x,y,z):
        self.w=0
        super().__init__(x,y,z,self.w)
        

s = Vector(1,2,3)
print(s.w)

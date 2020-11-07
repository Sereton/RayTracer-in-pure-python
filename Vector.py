from  BasicTuple import BasicTuple
from math import sqrt
class Vector(BasicTuple):
    def __init__(self,x,y,z):
        
        super().__init__(x,y,z,0)

    
    def magnitude(self):
        """ Returns the magnitude of the vector
        """
        return sqrt(sum(a * a for a in (self.x,self.y,self.z)))

    def normal(self):
        """ Returns the equivalent unit vector
        """
        return  self/self.magnitude()

    def cross(self,other):
        """ Returns the cross product AxB
        """
        x= (self.y)*(other.z)-(self.z)*(other.y)
        y= (self.z)*(other.x)-(self.x)*(other.z)
        z= (self.x)*(other.y) -(self.y)*(other.x)

        return self.__class__(x,y,z)

    
    
    
        
      

    def __iter__(self):
        self.values = (self.x,self.y,self.z,self.w)
        return self.values.__iter__()
    
    
    
    def __getitem__(self, key):
        
        return self.values[key]
        


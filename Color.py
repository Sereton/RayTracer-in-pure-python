from  BasicTuple import BasicTuple

class Color(BasicTuple):
    """Color class, represented as a 4-tuple to inherit from BasicTuple and 
    to have the chance to extend later with a RBGH value
    """

    def __init__(self,x,y,z):
        super().__init__(x,y,z,"")

    
    def __mul__(self,other):
        x=self.x * other.x
        y=self.y * other.y
        z=self.z * other.z
        return self.__class__(x,y,z)

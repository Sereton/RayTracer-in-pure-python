from  BasicTuple import BasicTuple

class Color(BasicTuple):
    """Color class, represented as a 4-tuple to inherit from BasicTuple and 
    to have the chance to extend later with a RBGH value
    """

    def __init__(self,x,y,z):
        super().__init__(x,y,z,0)

    
    def __mul__(self,other):
        if type(other) == type(self):
            x=self.x * other.x
            y=self.y * other.y
            z=self.z * other.z
            return self.__class__(x,y,z)
        elif type(other) == type(1) or type(other) == type(1.0):
            product = tuple( a * other for a in self )[:3]
            return  self.__class__(*product)
        
    
    def clampcolor(self,minval,maxval):
        x= max(minval,min(maxval,self.x))
        y= max(minval,min(maxval,self.y))
        z= max(minval,min(maxval,self.z))
        return Color(x,y,z)
    def __str__(self):
        return f'{self.x} {self.y} {self.z} '

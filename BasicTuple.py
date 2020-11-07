class BasicTuple:
    def __init__(self,x,y,z,w):
        self.x = x
        self.y = y
        self.z= z
        self.w =w

    def __str__(self):
        return f'<{self.x},{self.y},{self.z},{self.w}>'

    def __add__(self,other):
        if(self.w==1 and self.__class__ == other.__class__): #not point+point allowed
            raise ArithmeticError("2 Points cannot be added")
        x= self.x + other.x
        y= self.y + other.y
        z= self.z + other.z
        w = self.w+ other.w
        finalclass=  other.__class__ if (self.w== 0) else self.__class__ # to dinamically pick the right class
        result = finalclass(x,y,z)
        return result

    def __sub__(self,other):
        if(self.w==0 and other.w==1): #not vector - point allowed
            raise ArithmeticError("A point cannot be substracted from a Vector")
        x= self.x - other.x
        y= self.y - other.y
        z= self.z - other.z
        
        
        
        return self.__class__(x,y,z)

    def dot(self, other):
        """ Returns the dot product (inner product) of self and other vector minus the
        """
        return sum(a * b for a, b in zip(self, other))
    
    def __mul__(self, other):
        """ Returns the dot product of self and other if multiplied
            by another Vector.  If multiplied by an int or float,
            multiplies each component by other.
        """
        if type(other) == type(self):
            return self.dot(other)
        elif type(other) == type(1) or type(other) == type(1.0):
            product = tuple( a * other for a in self )[:3]
            return  self.__class__(*product)
    def __truediv__(self, other):
        """ Returns the dot product of self and other if multiplied
            by another Vector.  If multiplied by an int or float,
            multiplies each component by other.
        """
        
        if type(other) == type(1) or type(other) == type(1.0):
            product = tuple( (a / other) for a in self )[:3]
            return  self.__class__(*product)
        
        raise ArithmeticError
        


    def __iter__(self):
        self.values = (self.x,self.y,self.z,self.w)
        return self.values.__iter__()
    
    
    
    def __getitem__(self, key):
        
        return self.values[key]
        


    def __neg__(self):
        x= -self.x 
        y= -self.y 
        z= -self.z 
        

        return self.__class__(x,y,z)
         


    
from Vector import Vector
from Point import Point

def main():
    g = Vector(0,-9.85,0)
    Pos = Vector(0,10,0)
    V= Vector(1,2,0).normal()*10
    deltat=0.001





    while(Pos.y>0):
        Pos = Pos + V* deltat
        V = V + g*deltat
    
    print(Pos,V)

if __name__=="__main__":
    main()
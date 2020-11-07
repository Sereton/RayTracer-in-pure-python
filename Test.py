from Vector import Vector
from Point import Point
from Canvas import Canvas
from Color import Color

def main():
    file_name='pruebita.ppm'
    g = Vector(0,-9.85,0)
    Pos = Vector(-400,-250,0)
    V= Vector(1,2,0).normal()*110
    deltat=0.01
  
    red = Color(1,0,0)
    white = Color(1,1,1)
    canvas = Canvas(1280,768)





    # while(Pos.y>-300):
    #     Pos = Pos + V*deltat
    #     V = V + g*deltat 
    #     canvas.write_pixel(int(Pos.x+640),int(384-Pos.y),white)

    for x in range(-300,300):
        for y in range(-300,300):
            if((x**2+y**2)<300**2):
                canvas.write_pixel(int(x+640),int(384-y),red)

    
    fp =open(file_name,'w')
    fp.write(canvas.toPPM())
    fp.close()

if __name__=="__main__":
    main()
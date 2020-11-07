from Color import Color

class Canvas:

    def __init__(self,W,H,color=Color(0,0,0)):
        self.width = W
        self.height = H
        self.MAX_COLOR_NUMBER = 255
        self.screen=[[str(color* self.MAX_COLOR_NUMBER)  for w in range(self.width)] for h in range(self.height)]


    def write_pixel(self,x,y,color):

        color = color.clampcolor(0,1)
            
        self.screen[y][x] = str(color*self.MAX_COLOR_NUMBER)
     
    def toPPM(self):
        l1 = "P3\n"
        l2= f'{self.width} {self.height}\n'
        l3=f'{self.MAX_COLOR_NUMBER}\n'
        file_text = l1+l2+l3
        for i in range(self.height):
            for j in range(self.width):
                file_text += self.screen[i][j]
            file_text += '\n'
        return file_text



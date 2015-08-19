from tealight.art import (color, line, spot, circle, box, image, text, background)

from math import sin, cos, pi

def star(x, y, c, sizex, sizey, spines):
  
  color(c)
  
  angle = 0
  
  for i in range(0, spines):
    x0 = x + (sizex * cos(angle))
    y0 = y + (sizey * sin(angle))
    
    line(x, y, x0, y0)
    
    angle = angle + (2 * pi / spines)

star(300, 300, "blue", 100,200, 50)
star(600, 400, "purple", 200,300, 100)
star(450, 200, "orange", 125,400, 30)
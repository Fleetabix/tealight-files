from tealight.art import (color, line, spot, circle, box, image, text, background)

x = -500
y = 150

width = 20
height = 20

for i in range(0,width):
  for j in range(0,height):
    if i % 4 == 0:
      image(x + (i+j) * 60, y + j * 60, "misc/YellowFlower.png")
    else:
      image(x + (i+j) * 60, y + j* 60, "misc/Clover.png")
     

from tealight.logo import move, turn
def width=200
def polygon(edges, size):
  angle = 360.0 / edges
  for i in range(0, edges):
    move(size)
    turn(angle)
   
def grid(rows, columns):
  turn(90)
  move(width/rows)
  turn(-90)
  move(width)

polygon(4,width)


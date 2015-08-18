from tealight.logo import move, turn

def polygon(edges, size):
  angle = 360.0 / edges
  for i in range(0, edges):
    move(size)
    turn(angle)
   
def grid(rows, columns, width):
  turn(90)
  move(width/rows)
  turn(-90)
  move(width)


polygon(4,200)
grid(8,8,200)

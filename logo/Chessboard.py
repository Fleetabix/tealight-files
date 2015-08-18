from tealight.logo import move, turn

def polygon(edges, size):
  angle = 360.0 / edges
  for i in range(0, edges):
    move(size)
    turn(angle)
   
def grid(rows, columns, width):
  for i in range(0,columns):
    turn(90)
    move(width/rows)
    turn(-90)
    move(width)
    move(-(width))
  turn(90)
  move(-(width))
  for i in range(0,rows):
    move(width/rows)
    turn(90)
    move(width)
    move(-(width))
    turn(-90)
    
    
  


polygon(4,200)
grid(8,8,200)

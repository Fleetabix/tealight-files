from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)

# This is a fairly useless algorithm!
dir=1
while True:
  move()
  
  if touch() == "wall":
    turn(2)
  
  turn(dir)
  move()
  dir=-dir
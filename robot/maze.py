from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
collision = False

while True:
  move()
  if touch() == "wall" and collision == False:
    turn(1)
    collision=True
  elif touch() == "wall" and collision == True:
    turn(2)
  else:
    collision=False
  
  

  
   
    
    
    
    
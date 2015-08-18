from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
collision_1 = False
collision_2=False
tryright=False
while True:
  move()
  if left_side() != "wall":
    turn(-1)
  if right_side() != "wall":
    turn(1)
  if right_side() != "wall" and left_side() != "wall":
    if tryright==False:
      turn(1)
      tryright=True
    Else:
      turn(-1)
      tryright=False
  if touch() == "wall" and collision_1 == False:
    turn(1)
    collision_1=True
  elif touch() == "wall" and collision_1 == True:
    turn(2)
    collision_1=False
    collision_2=True
  elif touch() == "wall" and collision_2==True:
    turn(-1)
  else:
    collision_1=False
    collision_2=False
  
  
  

  
   
    
    
    
    
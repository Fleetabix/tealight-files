from tealight.robot import (move, 
                            turn, 
                            look, 
                            touch, 
                            smell, 
                            left_side, 
                            right_side)
collision_1 = False
collision_2=False
while True:
  move()
  if touch() == "wall" and collision_1 == False:
    turn(1)
    collision_1=True
  elif touch() == "wall" and collision_1 == True:
    turn(2)
    collision_1=False
    collision_2=True
  elif touch() == "wall" and collision_2==True:
    turn(3)
  else:
    collision_1=False
    collision_2=False
  
  

  
   
    
    
    
    
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
tryleft=False
while True:
  move()
  if left_side() != "wall" and right_side()=="wall":
    turn(-1)
  elif right_side() != "wall" and left_side()=="wall":
    turn(1)
  elif right_side() != "wall" and left_side() != "wall":
    'if tryright==False:
    '  turn(1)
    '  tryright=True
    'elif tryleft==False:
    '  turn(-1)
    '  tryleft=True
    'else:
     ' turn(2)
     ' tryright=False
     ' tryleft=False
    turn(-1)
    
    
    
   
   
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
  
  
  

  
   
    
    
    
    
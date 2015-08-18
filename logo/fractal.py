from tealight.logo import move, turn

# Draws the von Koch Snowflake curve

def segment(scale, detail):
  
  if detail == 0:
    for i in range (0, 3):
    move(scale)
    turn(-120)
  else:
    segment(scale / 3.0, detail - 1)
    turn(-60)
    segment(scale / 3.0, detail - 1)
    turn(120)
    segment(scale / 3.0, detail - 1)
    turn(-60)
    segment(scale / 3.0, detail - 1)
    

turn(90)
move(-300)
segment(600,0)
move(-300)
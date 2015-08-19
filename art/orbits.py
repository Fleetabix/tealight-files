from tealight.art import (color, line, spot, circle, box, image, text, background)

from tealight.art import screen_width, screen_height

x = screen_width / 2
y = screen_height / 2
vx = 0
vy = 0
ax = 0
ay = 0

power = 0.3

def handle_keydown(key):
  global ax, ay
  

  if key == "left":
    if x<screen_width / 2:
      ax = -power+0.05
    else:
      ax = -power-0.05
  elif key == "right":
    if x>screen_width / 2:
      ax = power-0.05
    else:
      ax=power+0.05
  elif key == "up":
    if y>screen_width / 2:
      ay = power-0.05
      
    else:
      ay=power+0.05
  elif key == "down":
    if y<screen_width / 2:
      ay = -power-0.05
    else:
      ay=-power+0.05
    
while True
def handle_keyup(key):
  global ax, ay
  
    if key == "left" or key == "right":
      if x<screen_width / 2:
        ax=.05
      else:
        ax=-.05
    elif key == "up" or key == "down":
      if y<screen_width / 2:
        ay=-0.05
      else:
        ay=0.05
    
def handle_frame():
  global x,y,vx,vy,ax,ay
  
  color("white")
  
  spot(x,y,8)
  vx = vx + ax
  vy = vy + ay
  
  x = x + vx
  y = y + vy
  
  color("blue")
  
  spot(x,y,8)
  
  

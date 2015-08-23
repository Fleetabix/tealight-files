print "Mineswepper"

size = 70
from github.fleetabix.art.Minesweeper import *
from github.AimeeH.art.Minesweeper import *
a = startx
b = starty
global uncoveredCells
uncoveredCells = 0
mineNumber = 20
global gameEnded
gameEnded = 0
#covers = [[]] * 10 # Placeholders for the two arrays of the map
#mines = [[]] * 10
#for i in range (0, 9):
  #covers[i] = [0] * 10
  #mines[i] = [0] * 10
  
def extension(x,y):
  for i in range(-1,2):
    for j in range (-1,2):
      if verify(i,x,j,y)==True:
        if mines[x+i][y+j]==0 and covers[x+i][y+j]==1:
          uncoverCell(x+i,y+j)
          extension(x+i,y+j)        
        elif mines[x+i][y+j]>0:
          uncoverCell(x+i,y+j)
  
def showMines():
  for i in range (0, 10):
    for j in range (0,10):
      if mines[i][j] == -1:
        uncoverCell(i, j)
  
def uncoverCell(x, y):
  global uncoveredCells
  global gameEnded
  if covers[x][y] == 1:
    uncoveredCells += 1
    covers[x][y] = 0
    show_num(x, y, mines[x][y])
    if mines[x][y] == -1:
      gameOver(x,y)
      showMines()
      gameEnded = 1
    elif mines[x][y] == 0:
      extension(x, y)
    if uncoveredCells == (100 - mineNumber):
      gameEnded = 1
      youWin(x, y)
      
  
def flagCount(x,y):
  flags = 0
  for i in range(-1,2):
    for j in range (-1, 2):
      if (i != 0) or (j != 0):
        if (x+i >= 0) and (x+i <= 9) and (y+j >= 0) and (y+j <= 9):
          if covers[x+i][y+j] == 2:
            flags += 1
  return flags
  
def uncoverGroup(x, y): # For uncovering a group of things
  if covers[x][y] == 0:
    flags = flagCount(x, y)
    if flags == mines[x][y]:
      for i in range (-1, 2):
        for j in range (-1, 2):
          if (i != 0) or (j != 0):
            if (x+i >= 0) and (x+i <= 9) and (y+j >= 0) and (y+j <= 9):
              if covers[x+i][y+j] == 1:
                uncoverCell(x+i, y+j)
  
  
def toggleFlag(x, y):
  if covers[x][y] == 1:
    covers[x][y] = 2
    flag(x,y)
  elif covers[x][y] == 2:
    covers[x][y] = 1
    removeFlag(x,y)


def handle_mouseup(x,y,button): # Detect mouse let go
  global gameEnded
  x = x - a
  y = y - b
  x = (x - (x % size))/size
  y = (y - (y % size))/size
  if (x >= 0) and (x <= 9) and (y >= 0) and (y <= 9) and (gameEnded == 0):
    if button == "left":  # Uncover cell
      uncoverCell(x, y)
    elif button == "middle":  # Auto-uncover group
      uncoverGroup(x, y)
    elif button == "right":   # Toggle flag
      toggleFlag(x, y)


#grid(a,b)

MineGen(mineNumber)
NumberGen()
#welcome()
grid(startx, starty)
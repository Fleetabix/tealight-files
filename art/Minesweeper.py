import (random)
mines = [[]] * 10 

for i in range(0,9):
  mines[i] = [0] * 10 
  
    
def MineGen(MineNumber):
  counter=0
  while counter<MineNumber:
    tempx=random.randint(0,9)
    tempy=random.randint(0,9)
    if mines[tempx][tempy]!=1:
      mines[tempx][tempy]=1
      counter=counter+1

MineGen(10)


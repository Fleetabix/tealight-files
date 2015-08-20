import random
mines = [[]] * 10 


  
def MineGen(MineNumber):
  counter=0
  while counter<MineNumber:
    tempx=random.randint(1,9)
    tempy=random.randint(1,8)
    if mines[tempx][tempy]!=1:
      mines[tempx][tempy]=1
      counter=counter+1

for i in range(0,9):
  mines[i] = [0] * 10    

MineGen(10)

for i in range(0,9):
  for j in range (0,9):
    print mines[i][j]
  



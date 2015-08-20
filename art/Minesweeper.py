import random
mines = [[]] * 10 


  
def MineGen(MineNumber):
  counter=0
  while counter<MineNumber:
    tempx=random.randint(0,9)
    tempy=random.randint(0,9)
    print tempx
    print tempy
    if mines[tempx][tempy]!=-1:
      mines[tempx][tempy]=-1
      counter=counter+1
  
def NumberGen():
  for i in range (0,9):
    for j in range (0,9):
      if mines[i][j]==-1:
        for a in range (-1,1):
          for b in range (-1,1):
            if mines[i+a][j+b]!=-1:
              mines[i+a][j+b]=mines[i+a][j+b]+1
              
      

for i in range(0,10):
  mines[i] = [0] * 10   

MineGen(10)

for i in range(0,9):
 for j in range (0,9):
  print mines[i][j]
  



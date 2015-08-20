import random
  
def MineGen(MineNumber):
  counter=0
  while counter<MineNumber:
    tempx=random.randint(0,9)
    tempy=random.randint(0,9)
    if mines[tempx][tempy]!=-1:
      mines[tempx][tempy]=-1
      counter=counter+1
  
def NumberGen():
  for i in range (0,9):
    for j in range (0,9):
      mineCount = 0
      #if mines[i][j]==-1:
       # for a in range (-1,1):
        #  for b in range (-1,1):
         #   if i+a<=9 and i+a>=0 and j+b<=9 and j+b>=0: 
          #    if mines[i+a][j+b]!=-1:
           #     mines[i+a][j+b]=mines[i+a][j+b]+1
      if mines[i][j]!=-1:
        for a in range (-1,1):
          for b in range(-1,1):
            if verify(i,a,j,b)==True:
              if mines[i+a][j+b]==-1:
                mineCount += 1
        mines[i][j] = mineCount
            
def Extension(x,y):
  for i in range(-1,2):
    for j in range (-1,2):
      if verify(i,x,j,y)==True:
        if mines[x+i][y+j]==0:
          uncoverCell(x+i,y+j)
          Extension(x+i,y+j)        
        elif mines[x+i][y+j]>0:
          uncoverCell(x+i,y+j)
              
              
def verify(num1,num2,num3,num4):
  if (num1+num2<10) and (num1+num2>-1) and (num3+num4<10) and (num3+num4>-1):
    return True
  else:
    return False
              
mines = [[]] * 10 
for i in range(0,10):
  mines[i] = [0] * 10 

covers = [[]] * 10 
for i in range(0,10):
  covers[i] = [1] * 10 
for i in range(-1,2):
  print i
 

#MineGen(50)
#NumberGen()
#for i in range(0,9):
 #for j in range (0,9):
  #print mines[i][j]
  



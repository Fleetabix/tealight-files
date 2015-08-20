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
      #if mines[i][j]==-1:
       # for a in range (-1,1):
        #  for b in range (-1,1):
         #   if i+a<=9 and i+a>=0 and j+b<=9 and j+b>=0: 
          #    if mines[i+a][j+b]!=-1:
           #     mines[i+a][j+b]=mines[i+a][j+b]+1
      print "Hi"        
def Extension(x,y):
  for i in range(-1,1):
    for i in range (-1,1):
      if i+x<=9 and i+x>=0 and j+y<=9 and j+y>=0:
        if mines[x+i][y+j]==0:
          uncoverCell(x+i,y+j)
          Extension(x+i,y+j)        
        elif mines[x+i][y+j]>0:
          uncoverCell(x+i,y+j)
              
              
              
              
mines = [[]] * 10 
for i in range(0,10):
  mines[i] = [0] * 10 

covers = [[]] * 10 
for i in range(0,10):
  covers[i] = [1] * 10 

 

#MineGen(50)
#NumberGen()
#for i in range(0,9):
 #for j in range (0,9):
  #print mines[i][j]
  



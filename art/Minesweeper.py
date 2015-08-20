Mines(9,9)

def MineGen(MineNumber):
  counter=0
  while counter<MineNumber:
    tempx=random.randint(0,9)
    tempy=random.randint(0,9)
    if mines(tempx,tempy)==1:
      mines(tempx,tempy)=1
      counter=counter+1

MineGen(10)
for i in range 0 to 9:
  for j in range 0 to 9:
    print Mines(i,j)

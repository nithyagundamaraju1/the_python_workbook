import random as rd
l=['H', 'T','H',"T"]
c=[]
hc=0
tc=0
nf=0
i=0
while i <= 10:
  c=rd.choice(l)
  while hc !=3 and tc != 3:
    nf=nf+1
    if c == 'H':
      print("H\t",end=" ")
      hc=hc+1
    if c=='T':
      print("T\t",end=" ")
      tc=tc+1
  hc=0
  tc=0
  print(f"{nf} flips",end="\n")
  nf=0  
  i=i+1
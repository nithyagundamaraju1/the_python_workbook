p=input("Enter 8 bits:")
while p!= " ":
  if p.count("0")+p.count("1") !=8 or len(p)!=8:
    print("Not eight bits!")
  else:
    ones=p.count("1")
  if ones%2==0:
    print("Parity is 0")
  else:
    print("Parity is 1")
  p=input("Enter 8 bits:")
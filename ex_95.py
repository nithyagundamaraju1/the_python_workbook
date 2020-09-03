def rand_license():
  import random as  rd
  import string
  on= rd.choice([0,1])
  lic=[]
  if on==0:
    print("\n-------------Old License------------")
    for i in range(0,3):
        let=rd.choice(string.ascii_uppercase)
        lic.append(let)
    for j in range(0,3):
        num=rd.randint(0,9)
        lic.append(num)
  else:
    print("\n-------------New License------------")
    for i in range(0,4):
        num=rd.randint(0,9)
        lic.append(num)
    for j in range(0,3):
        let=rd.choice(string.ascii_uppercase)
        lic.append(let)
  return lic

lic=rand_license()
for k in lic:
  print(k,end="")
print("\n")

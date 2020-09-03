def password():

  import random as rd
  len=rd.randint(7,10)
  print(f"length of the password: {len} ")
  i=0
  pwd=[]
  for i in range(0,len+1):
    n=rd.randint(33,126)
    p=chr(n)
    pwd.append(p)
  return pwd
  

psw=password()
print("The password is:",end=" ")
for j in psw:
  print(j,end="")

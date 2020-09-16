from ex_94 import password
from ex_96 import pwd_check 

good=False
count=0
while good==False:
  psw=password()
  res=pwd_check(psw)
  if  res == True:
    good=True
    break
  else:
    count=count+1 
print("The password is: ",end="\"")
for j in psw:
  print(j,end="")
print("\"")
print(f"\nNumber of attempts: {count}")

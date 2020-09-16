import string as s
def pwd_check(str):
  count=0
  for i in str:
    if i in s.ascii_uppercase:
      count=count+1
    if i in s.digits:
      count=count+1
    if i in s.punctuation:
      count=count+1
  if len(str)>=8 and count>=3:
    return True
  else:
    return False

str=input("Enter password:")
res=pwd_check(str)
if res==True:
  print("Good Password")
else:
  print("Password is not good")
       
  
  
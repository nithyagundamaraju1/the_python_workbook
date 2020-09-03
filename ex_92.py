def prime (num):
  if (num==1):
    return -1
  elif (num==2):
    return 1;
  else:
    for x in range(2,num):
      if(num % x==0):
        return -1
    return 1          

num = int(input("Enter a number: "))  
num=num+1
p=prime(num)
while p ==-1:
  num=num+1
  p=prime(num)
  
print(f"Nearest Prime: {num}")
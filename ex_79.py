import random as rd
lt=100
num=rd.randrange(0,10000)
max=num
count=0
print(max)
for i in range(1,lt+1):
  curr=rd.randrange(0,10000)
  if curr>max:
    max=curr
    count=count+1
    print(curr," is updated to",max)
  else:
    print(curr)
print("Maximum Number of the list:",max)
print("No of times it was updated:",count)
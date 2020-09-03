print("Enter three integers seperated by comma:")
p,q,r=input().split(",")
a=int(p)
b=int(q)
c=int(r)
x=max(a,b,c)
y=min(a,b,c)
z=a+b+c-x-y
print(f"Sorted Numbers: {y,z,x}")


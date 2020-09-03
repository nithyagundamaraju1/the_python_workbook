def isTriangle(a,b,c):
  s1=a+b
  s2=b+c
  s3=c+a
  if a>s2 or b>s3 or c>s1:
    return False
  else:
    return True

a=float(input("Enter side1:"))
b=float(input("Enter side2:"))
c=float(input("Enter side3:"))
p=isTriangle(a,b,c) 
if p:
  print(f"{a},{b}&{c} form a triangle")
else:
  print("No triangle")



           













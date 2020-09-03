p=float(input("Enter side1: "))
q=float(input("Enter side2: "))
r=float(input("Enter side3: "))
if p==q==r:
   print("Equilateral")
elif p==q or q==r or p==r:
   print("Isoceles")
else:
   print("Scalene")
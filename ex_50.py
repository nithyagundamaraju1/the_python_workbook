import math
a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))
disc= (b*b)-(4*a*c)
if disc < 0:
   print("No real roots")
elif disc==0 :
   print("One real root")
   root=-(b/(2*a))
   print(f"Real root is: {root:.02f}")
else:
   print("Two real roots")
   root1=(1/(2*a))*(-b+math.sqrt(disc))
   root2=(1/(2*a))*(-b-math.sqrt(disc))
   print(f"Real roots are: {root1:.02f} and {root2:.02f}")
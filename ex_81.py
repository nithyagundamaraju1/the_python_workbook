def hypotenuse():
  from math import sqrt
  c=sqrt(pow(a,2)+pow(b,2))
  return c




import math
a=float(input("Enter length of a:"))
b=float(input("Enter length of b:"))

hyp=hypotenuse()
print(f"Hypotenuse: {hyp:.02f} units")
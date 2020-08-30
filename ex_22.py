import math


s1=float(input("Enter the first side of a triangle:"))
s2=float(input("Enter the second side of a triangle:"))
s3=float(input("Enter the third side of a triangle:"))
s = (s1+s2+s3)/2
area=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))
print(f"Area of the triangle is {area:.02f} sq.units")

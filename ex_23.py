import math
s=float(input("Enter the side of polygon:"))
n=int(input("enter number of sides:"))
x= math.tan(math.pi/n)
area=(n*s*s)/(4*x)
print(f"Area of the polygon is {area:.02f} sq units")
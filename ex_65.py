import math
per=0
xx=float(input("Enter x of first point:"))
yy=float(input("Enter y of first point:"))
x1=xx
y1=yy

line=input("Enter the x part of next point (blank to quit): ")
while line !=" ":
    x=float(line)
    y=float(input("Enter y of coordinate:"))
    dist=math.sqrt(pow(x1-x,2)+pow(y1-y,2))
    per=per+dist
    x1=x
    y1=y
    line=input("Enter the x part of next point(blank to quit): ")
dist=math.sqrt(pow(xx-x,2)+pow(yy-y,2))
per=per+dist

print(f"Perimeter of polygon is: {per:.02f} units")
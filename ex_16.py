import math
r=float(input("Enter radius:"))
area=(math.pi*r*r)
vol=(4/3)*area*r
print(f"area of circle:{area:.02f} sq.units")
print(f"Volume of sphere:{vol:.02f} cu.units")

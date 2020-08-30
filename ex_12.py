from math import radians, cos, sin, asin, sqrt
lat1=float(input("Enter the latitude of first point: "))
lon1=float(input("Enter the longitude of first point: "))
lat2=float(input("Enter the latitude of second point: "))
lon2=float(input("Enter the longitude of second point: "))
lon1 = radians(lon1) 
lon2 = radians(lon2) 
lat1 = radians(lat1) 
lat2 = radians(lat2) 
dlon = lon2 - lon1  
dlat = lat2 - lat1 
a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * asin(sqrt(a))  
r = 6371
dist=c*r
print(f"Distance is {dist} kms")
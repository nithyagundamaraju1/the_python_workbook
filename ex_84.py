
def median(a,b,c):
 if a > b:
    if a < c:
        median = a
    elif b > c:
        median = b
    else:
        median = c
 else:
    if a > c:
        median = a
    elif b < c:
        median = b
    else:
        median = c  
 return median





a=int(input("enter a:" ))
b=int(input("enter b:" ))
c=int(input("enter c:" ))
med=median(a,b,c)
print(f"Median: {med}")
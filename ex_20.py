r=8.314
p=float(input("Enter pressure in pascals:"))
v=float(input("Enter volume in liters:"))
print("Enter temperature [eg:101 c if celsius or 101 f for fahreinheit] :")
a,b=input().split(" ")
t=float(a)
if b=='c':
   t=t+273.15
elif b=='f':
   t=5/9(t-32)+273.15
n=(p*v)/(r*t)
print(f"Amount of gas: {n} moles")
   

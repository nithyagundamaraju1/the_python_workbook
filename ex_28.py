ta=float(input("enter air temperature in celsius:"))
v=float(input("Enter the windspeed in kmph:"))
a=13.12
b=0.6215*ta
c=11.37*pow(v,0.16)
d=0.3965*ta*pow(v,0.16)
if ta<=10 and v>4.8 :
   wci=a+b-c+d
   print(f"\nWind Chill Index: {round(wci)}")
else:
   print("\n    Wind Chill Index is invalid!! ")
   print("It is only considered valid for temperatures <= 10 C and windspeeds > 4.8 kmph.")

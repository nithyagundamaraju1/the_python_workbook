r=float(input("Enter the rating:"))
a=0.0
b=0.4
c=0.6
amt=0
if r == a:
   print("Unacceptable performance")
   amt=r*2400.00
elif r==b:
   print("Acceptable Performance")
   amt=r*2400.00
elif r>=c:
   print("Meritorious Performance")
   amt=r*2400.00
elif r>a and r<b:
   print("Invalid Rating")
elif r>b and r<c:
   print("Invalid Rating")
if amt>0:
   print(f"The amount of the employee’s raise: {amt} ")

   
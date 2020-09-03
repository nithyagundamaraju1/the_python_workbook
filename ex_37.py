n=int(input("Enter number of sides: "))
if n > 10 or n< 3:
   print("Error!")
elif n==3:
   print("Triangle")
elif n==4:
   print("Square")
elif n==5:
   print("Pentagon")
elif n==6:
   print("Hexagon")
elif n==7:
   print("Septagon")
elif n==8:
   print("Octagon")
elif n==9:
   print("Nonagon")
else:
   print("Decagon")

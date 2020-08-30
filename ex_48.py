year = int(input("Input year: "))
n=year%12
if n == 8:
   print("Dragon")
elif n==9:	
   print("Snake")
elif n==10:
   print("Horse")
elif n==11:
   print("Sheep")
elif n==0:
   print("Monkey")
elif n==1:
   print("Rooster")
elif n==2:
   print("Dog")
elif n==3:
   print("Pig")
elif n==4:
   print("Rat")
elif n==5:
   print("Ox")
elif n==6:
   print("Tiger")
elif n==7:
   print("Hare")
else:
   print("Error!!")

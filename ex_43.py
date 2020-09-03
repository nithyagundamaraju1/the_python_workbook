n=int(input("Enter denomination of a banknote: "))
if n==1:
   print("George Washington ")
elif n==2:
   print("Thomas Jefferson")
elif n==5:
   print("Abraham Lincoln")
elif n==10:
   print("Alexander Hamilton")
elif n==20:
   print("Andrew Jackson")
elif n==50:
   print("Ulysses S. Grant")
elif n==100:
   print("Benjamin Franklin ")
else:
   print("appropriate error message")
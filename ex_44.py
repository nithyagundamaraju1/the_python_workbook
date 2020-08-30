m=input("Enter name of month: ")
n=int(input("Enter date: "))
if n == 1 and m=='january':
   print("New year’s day")
elif n==1and m=='july' :
   print("Canada day")
elif n==25 and m=='december' :
   print("Christmas day")
else:
   print("entered month and day do not correspond to a fixed-date holiday")

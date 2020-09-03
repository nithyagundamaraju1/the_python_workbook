m=input("Enter name of month: ")
n=int(input("Enter date: "))
if n == 20 and m=='march':
   print("Spring")
elif n==21 and m=='june' :
   print("Summer")
elif n ==22 and m=='december' :
   print("Winter")
elif n==22 and m=='september' :
   print("Fall")
else:
   print("entered month and day do not correspond to a fixed-date holiday")

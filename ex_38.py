n=input("Enter name of month: ")
if n in ('january','march','may','july','august','october','december'):
   print("31 days")
elif n in ('april','june','september','november'):
   print("30 days")
elif n == 'february':
   print("28 or 29 days")
else:
   print("Not a month!")

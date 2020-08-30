g=float(input("Enter your grade points:"))
if g>4.0:
   print("Grade:A+ ")
elif g==4.0:
   print("Grade:A")
elif g < 4.0 and g >= 3.7:
   print("Grade:A-")
elif g>=3.3 and g <3.7:
   print("Grade:B+")
elif g<3.3 and g>=3.0:
   print("Grade: B")
elif g<3.0 and g >=2.7:
   print("Grade:B-")
elif g >= 2.3 and g<2.7:
   print("Grade:C+")
elif g >= 2.0 and g<2.3:
   print("Grade:C")
elif g >= 1.7 and g<2.0:
   print("Grade:C-")
elif g >= 1.3 and g<1.7:
   print("Grade:D+")
elif g >= 1.0 and g<1.3:
   print("Grade:D")
elif g < 1.0 and g>=0:
   print("Grade: F")
else:
   print("Invalid!!")



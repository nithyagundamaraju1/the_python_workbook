w= int(input("Enter wavelength:"))
if w>=380 and w<450:
   print(f"Violet")
elif w>=450 and w<495:
   print(f"Blue")
elif w>=495 and w<570:
   print(f"Green")
elif w>=570 and w<590:
   print(f"Yellow")
elif w>=590 and w<620:
   print(f"Orange")
elif w>=620 and w<750:
   print(f"Red")
else: 
   print("Outside of the visible spectrum")



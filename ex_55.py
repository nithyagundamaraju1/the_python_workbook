w= int(input("Enter emr:"))
if w<(3*pow(10,9)):
   print("Radio waves")
elif w>=(3*pow(10,9)) and w<(3*pow(10,12)):
   print(f"Microwaves")
elif w>=(3*pow(10,12)) and w<(4.3*pow(10,14)):
   print(f"Infrared light")
elif w>=(4.3*pow(10,14)) and w<(7.5*pow(10,14)):
   print(f"Visible light")
elif w>=(7.5*pow(10,14)) and w<(3*pow(10,17)):
   print(f"Ultraviolet light")
elif w>=(3*pow(10,17)) and w<(3*pow(10,19)):
   print(f"X-rays")
elif w>=(3*pow(10,19)):
   print(f"Gamma rays")
else:
   print("Invalid emr")

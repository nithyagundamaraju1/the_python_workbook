mag=float(input("Magnitude of earth quake: "))
e='earthquake'
if mag < 2.0:
   print(f"Micro {e}")
elif 2.0 <= mag < 3.0:
   print(f"Very minor {e}")
elif 3.0 <=mag < 4.0:
   print(f"Minor {e}")
elif 4.0 <=mag < 5.0:
   print(f"Light {e}")
elif 5.0 <=mag < 6.0:
   print(f"Moderate {e}")
elif 6.0 <=mag < 7.0:
   print(f"Strong {e}")
elif 7.0 <=mag < 8.0:
   print(f"Major {e}")
elif 8.0 <=mag < 10.0:
   print(f"Great {e}")
else:
   print(f"Meteoric {e}")



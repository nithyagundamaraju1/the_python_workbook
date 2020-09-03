n=int(input("Number of loaves of day old bread being purchased:"))
print("Regular price: $3.49 each")
reg=n*3.49
dis=((60/100)*3.49)*n
tot=reg-dis
print(f"Regular Price: ${reg:.02f}")
print(f"Discount Rate: ${dis:.02f}")
print(f"Total Price  : ${tot:.02f}")






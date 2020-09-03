
print("Enter your ht [ex: if your ht is 5 feet 3 inches, enter it as 5 3]:")
ft,inch=input().split(" ")

cms=(int(ft)*12*2.54)+(int(inch)*2.54)
print(f"Your height in centimeters: {cms:.02f} cms")
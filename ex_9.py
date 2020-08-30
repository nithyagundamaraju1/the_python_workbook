r = 0.04
n=1
p=float(input("Enter the deposited amount:"))
for i in range(1,4):
   amt=p*pow((1+(r/n)),n*i)
   print(f"The amount after {i} year is {amt:.02f}")
   
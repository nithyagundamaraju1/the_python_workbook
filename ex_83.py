def shipping(n):
  pri=10.95+(2.95*n-1)
  return pri

n=int(input("number of items in the order: "))
p=shipping(n)
print(f"The shipping charge is {p:.02f}")
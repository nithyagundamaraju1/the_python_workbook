a=int(input("Enter a:"))
b=int(input("Enter b:"))
div=min(a,b)

while a%div != 0 or b%div != 0:
  div=div-1
print(f"GCD of {a} and {b} is {div}")
  
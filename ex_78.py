num=int(input("Enter a number to convert: "))
result=""
q=num
r=q%2
result=str(r)+result
q=q//2


while q > 0:
  r=q%2
  result=str(r)+result
  q=q//2

print(f" {num} in Decimal is {result} in binary")


  								

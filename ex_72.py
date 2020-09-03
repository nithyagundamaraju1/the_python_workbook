str=input("Enter palindrome:")
pal=True
for i in range(0,len(str)//2):
  if str[i] != str[len(str)-i-1]:
    pal = False
if pal:
  print("Palindrome!")
else:
  print("Not a Palindrome!") 
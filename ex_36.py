ch=input("Enter an alphabet:")

if ch in ('a','e','i','o','u') :
   print("Vowel")
elif ch=='y':
   print("Either consonant or vowel")
else:
   print("Consonant")
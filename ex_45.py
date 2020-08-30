m=input("Enter column: ")
n=int(input("Enter row: "))
if m in ('a','c','e','g') and n%2==0:
   print("white")
elif m in ('a','c','e','g') and n%2 != 0:
   print("black")
elif m in ('b','d','f','h') and n%2 != 0:
   print("white")
elif m in ('b','d','f','h') and n%2 == 0:
   print("black")
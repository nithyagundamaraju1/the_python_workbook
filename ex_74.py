min=1
max=10

print("   ",end=" ")
for i in range(1,11):
  print(f"{i:5d}",end=" ")
print("\n\t--------------------------------------------------------")
for i in range(1,11):
  print(f"{ i:4d}",end="| ")
  for j in range(1,11):
    print(f"{i*j:4d}",end="| ")
  print()
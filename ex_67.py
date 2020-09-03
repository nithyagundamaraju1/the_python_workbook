a=input("Enter age..To end please enter blank:")
tot=0
while a != " ":
  age=int(a)
  if age<=2:
    tot=tot+0
  elif age<=12:
    tot=tot+14
  elif age<=64:
    tot=tot+18
  a=input("enter price..To end please enter blank:")
print(f"Group Total: ${tot:.02f}")
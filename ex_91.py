def precedence(str):
  ch=[]
  oper=[]
  pre=[]
  for i in str:
    oper.append(i) if i in op else ch.append(i)
  print("Characters:",end=" ")
  print(ch,end=",")
  print("Operators:",end=" ")
  print(oper,end=",")
  for i in oper:  
    if i=='+' or i == '-':
      pre.append(1)
    elif i=='*' or i == '/':
      pre.append(2)
    elif i=='^':
      pre.append(3)
    else:
      pre.append(0)
  return pre 




p=[]
op=['+','-','*','/','//','%','**','==','!=','<',' >','<=','>=','is','in','and','not','or','(','&','|','~','^','<<','>>',')','^']
str=input("Enter the expression: ")
p=precedence(str)
print(f"Precedence of operators is :",end=" ") 
print(p)
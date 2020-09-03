width=80
def center(s,wid):
  if wid < len(s):
    return s
  spaces= (wid-len(s))//2
  result= "" * spaces + s
  return result
def main():
  print(center("***********************************************************",width))
  print(center("-------------------^_^^_^^_^-------------------\n",width))
  print(center(" Nithya ",width))
  print(center("\n-----------------^_^^_^^_^---------------------",width))
  print()
  print("************************************************************")

main()
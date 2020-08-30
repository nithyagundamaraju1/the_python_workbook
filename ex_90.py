def isInteger(s):
  s=s.strip()
  if(s[0] == "+" or s[0]== "-") and s[1:].isdigit():
    return True
  if s.isdigit():
    return True
  return False
def main():
  s=input("Enter a string: ")
  if isInteger(s):
    print("String represents an integer.")
  else:
    print("String doesn't represents an integer.") 
if __name__=="__main__":
  main()
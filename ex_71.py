x=float(input("Enter number:"))
guess=x/2
good=(guess*guess)-x
while abs(good) <= pow(10,-12) :
   guess= (guess+(x/guess))/2
   x=guess
   good=(guess*guess)-x
print(f"Square root : {guess}")
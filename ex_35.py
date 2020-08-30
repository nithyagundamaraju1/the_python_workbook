n=int(input("Enter human years:"))
 
if n>0 and n<=2:
   dog_yr=n*10.5
   print(f"Dog years: {dog_yr:.01f} years")
elif n>2:
   dog_yr=(2*10.5) + (n-2)*4
   print(f"Dog years: {dog_yr} years")
else:
    print("Negative Integer is Invalid!!")
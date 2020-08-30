pri=input("enter price..To end please enter blank:")

sum=0
while pri != " ":
    
    sum=sum+float(pri)
    pri=input()

print(f"Total amount: {sum:.02f}")
#for this amount--pennies is (sum*100)--so  the amount paid using nickels is the runding indicator
ri= (sum*100)%5 

if ri < 2.5:
     total=sum-(ri/100)
else:
     total=sum+0.05-(ri/100)
print(f"Cash payable: {total:.02f}")
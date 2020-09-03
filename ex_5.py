less=int(input("Enter the number of containers holding less than or equal to one litre: \n"))
more=int(input("Enter the number of containers holding greater than one litre: \n"))
refund= float((0.10* less)+(0.25*more))

print("Refunded amount: $"+"{:.2f}".format(refund))
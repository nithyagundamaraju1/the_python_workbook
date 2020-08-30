sum = 0.0
count = 0
while(1):
    x=int(input("Enter Values: "))
    if x == 0:
        print("End of input.")
        break;
    sum+=x;
    count+=1;
if count == 0:
    print("No input given")
else:
    avg = sum/count;
    print("Average is - ",avg)
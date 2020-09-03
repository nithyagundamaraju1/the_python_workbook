import random
r=['0','00', 1,2,3,4,5,6,7,8, 9,10,11,12,13, 14, 15,16,17,18, 19,20, 21,22,23,24, 25,26, 27, 28,29,30,31,33,32,34,35,36]
roul=random.choice(r)
print(f"The spin resulted in {roul}...")
if roul in ('0','00'):
    print(f"Pay {roul}")
    exit()
else:
    print(f"Pay {roul}")
    if roul in (1,3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30,32, 34,36):
        print("Pay Red")
    elif roul in ('0','00'):
        print("Pay Green")
    else:
        print("Pay Black")
    if roul % 2==0:
        print("Pay Even")
    else: 
        print("Pay Odd")
    if roul in [1-18]:
        print("Pay 1 to 18")
    else:
        print("Pay 19 to 36")


def leap():
    if yr % 4 == 0 and yr % 100 != 0:
        return 1
    elif yr % 100 == 0:
        return 0
    elif yr % 400 ==0:
        return 1
    else:
        return 0
 	
day = int(input("Enter Day: "))
mnth = int(input("Enter Month: "))
yr = int(input("Enter Year: "))
if day>31 and mnth>12:
    print("Invalid date")
    exit()
l=leap()
if day==28 and mnth==2:
    if l!=1:
        day=1
        mnth=mnth+1
    else :
        day=29 
elif day==30 and mnth in (4,6,9,11) :
    day=1
    mnth=mnth+1
elif day==30 and mnth in (1,3,5,7,8,10,12):
    day=day+1
elif day==31 and mnth==12:
    day=1
    mnth=mnth+1
    yr=yr+1
elif day<28:
    day=day+1
elif day==29 and mnth==2:
    day=1
    mnth=mnth+1
elif day==31 and mnth in (1,3,5,7,8,10,12):
    day=1
    mnth=mnth+1
print(f"Next day: {day:02d}-{mnth:02d}-{yr}")

    
   
    
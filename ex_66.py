g=input("Enter your grade(blank to quit): ")
if g=='A+' or g=='a+':
    gp=4.0
elif g=='A' or g=='a':
    gp=4.0
elif g=='A-' or g=='a-':
    gp=3.7
elif g=='B+' or g=='b+':
    gp=3.3
elif g=='B' or g=='b':
    gp=3.0
elif g=='B-' or g=='b-':
    gp=2.7
elif g=='C+' or g=='c+':
    gp=2.3
elif g=='C' or g=='c':
    gp=2.0
elif g=='C-' or g=='c-':
    gp=1.7
elif g=='D+' or g=='d+':
    gp=1.3
elif g=='D' or g=='d':
    gp=1.0
elif g=='F' or g=='f':
    gp=0
sum=gp
count=0
while g !=" ":

   g=input("Enter your grade(blank to quit): ")
   
   
   if g=='A+' or g=='a+':
      gp=4.0
   elif g=='A' or g=='a':
      gp=4.0
   elif g=='A-' or g=='a-':
      gp=3.7
   elif g=='B+' or g=='b+':
      gp=3.3
   elif g=='B' or g=='b':
      gp=3.0
   elif g=='B-' or g=='b-':
      gp=2.7
   elif g=='C+' or g=='c+':
      gp=2.3
   elif g=='C' or g=='c':
      gp=2.0
   elif g=='C-' or g=='c-':
     gp=1.7
   elif g=='D+' or g=='d+':
     gp=1.3
   elif g=='D' or g=='d':
     gp=1.0
   elif g=='F' or g=='f':
     gp=0

   sum=sum+gp
   count=count+1
gpa=(sum/(count+1))
print(f"Grade point Average: {round(gpa,1)}")
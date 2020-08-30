n=int(input("Sound level in decibels: "))
if n > 130 :
   print("Louder than Jackhammer !")
elif n==130:
   print("Jackhammer")
elif n in range(107,130):
   print("In the range of Jackhammer and Gas lawnmower")
elif n==106:
   print("Gas lawnmower")
elif n in range(71,106):
   print("In the range of Gas lawnmower and Alarm clock ")
elif n==70:
   print("Alarm clock")
elif n==40:
   print("Quiet room")
elif n in range(41,70):
   print("In the range of Alarm clock and Quiet room ")
else :
   print("Quieter than Quiet room!")
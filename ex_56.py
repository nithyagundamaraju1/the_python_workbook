min=int(input("Enter number of minutes   :"))
msg=int(input("Enter number of messages  :"))
base=15.00
fee= 0.44
print(f"Base Charges              :$ {base:.02f}")
print(f"Addl.Charges for 911 Calls:$ {fee:.02f}")
if min<=50 and msg<=50:
   sum=base+fee
  
elif min>50 and msg >50:
   x=min-50
   y=msg-50
   sum=(x*.25)+(y*.15)+base+fee
   print(f"Addl Charges for airtime  :$ {x* 0.25:.02f}")
   print(f"Addl Charges for messages :$ {y*0.15:.02f} ")
tax= 0.05*sum 
tot_amt= sum + tax
print(f"Tax amount for the bill   :$ {tax:.02f}")  
print(f"Total Bill Amount         :${tot_amt:.02f}")
 
    

   


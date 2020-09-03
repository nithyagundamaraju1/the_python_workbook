BASE = 4.00
VARIABLE = 0.25
 
def taxi_fare(dist):
   
    units = (dist*1000) / 140
    total = units * VARIABLE
    total = total+BASE
    return total

dist=float(input("Enter distance in kms: "))
fare= taxi_fare(dist)
print(f"The fare is $ {fare:.02f}")
            

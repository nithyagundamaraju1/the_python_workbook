p=float(input("Enter pressure in Kilo Pascals:"))
psi=(p/6.895)
mmhg= p/7.501
atm=p/101
print("-------------Equivalent pressure in various scales-------------")
print(f"Pounds per sq.inch :    {round(psi,2)} psi")
print(f"Millimeters of mercury: {round(mmhg,2)} mmHg")
print(f"Standard Atmosphere:    {round(atm,2)} atm") 




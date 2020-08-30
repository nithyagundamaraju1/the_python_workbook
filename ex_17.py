c= 4.186
cost=8.9 
m=float(input("Enter mass of water:"))
dt=float(input("Enter difference of temperature:"))
q_j= m*dt*c
q_kw= q_j/3600000
print(f"Total energy required: {q_j:.03f} Joules or {q_kw:.03f} Kwh")
print(f"Electricity cost= {cost} cents per Kwh")
bill=(q_kw*cost)/100
print(f"Bill Amount: ${bill:02f}")

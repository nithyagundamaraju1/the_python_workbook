n = int(input("Please enter a value for N:"))
total=0
for i in range(1,n):
        total += (-1)**(i+1)*((1.0/(i+i+1)))
value = 4*(1-total)
print(value)




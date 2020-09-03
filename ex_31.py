num=int(input("Enter a four digit numbers: "))
sum=0
while (num != 0): 
        sum = sum + int(num % 10) 
        num = int(num/10) 
print(f"The sum of digits:{sum}")
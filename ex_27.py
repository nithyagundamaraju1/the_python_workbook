wt=float(input("Enter your weight in kgs: "))
ht=float(input("Enter your height in cms: "))
ht=ht/100
bmi= wt/(ht*ht)
print(f"Your BMI: {bmi:.02f}")

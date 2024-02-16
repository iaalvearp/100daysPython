height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))
bmi = round(weight/(height * height))

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you're underweight!")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you've normal weight!")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you're overweight!")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you're obese!")
else:
    print(f"Your BMI is {bmi}, you're clinically obese!")
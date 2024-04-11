height = float(input("Input your height in Meters."))
weight = float(input("Input your weight in Kgs."))


bmi = round((weight / height ** 2), 2)
# bmi = (weight / height ** 2)
# print(round(bmi,2))

if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you are normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

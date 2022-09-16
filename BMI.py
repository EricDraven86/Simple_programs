body_mass = float(input("Enter your body weight: "))
height = float(input("Enter your height in cm: "))

BMI = body_mass/((height/100)**2)

print("\nYour BMI is: ", round(BMI, 2))


if BMI >= 40:
    print("Obesity (Class 3)")
elif BMI >= 35:
    print("Obesity (Class 2)")
elif BMI >= 30:
    print("Obesity (Class 2")
elif BMI >= 25:
    print("Over weight")
elif BMI >= 18.5:
    print("Normal weight")
else:
    print("Under weight")
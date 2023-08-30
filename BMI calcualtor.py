# this program calculates BMI( Body Mass Index)
# BMI waa hab aad ku ogaan karto Misaanka jirkaaga inuu yahay mid normal ama mid caato aha ama mid aad u weyn;
# Get weight and height from user
weight = int(input("enter your weight: "))
height = float(input("Enter your height: "))
# calculating BMI
BMI = weight / height ** 2
# check bmi category
if BMI < 18.5:
    print("Underweight")

elif BMI >= 18.5 and BMI < 25:
    print("Normal")

elif BMI >= 25 and BMI < 30:
    print("Overweight")

else:
    print("Obesity")

print(f"{BMI:.2f}")
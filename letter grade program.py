# Ask the user to enter a test score
OVER_SCORE = 100
UNDER_SCORE = 0
A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60
F_SCORE = 50
score = float(input("Enter a test score: "))
# Determine if the grade is grater than 100 and less than 0:
if score > OVER_SCORE or score < UNDER_SCORE:
    print('invalid grade')
elif score >= A_SCORE:
    print("your grade is A")
elif score >= B_SCORE:
    print("your grade is B")
elif score >= C_SCORE:
    print("your grade is C")
elif score >= D_SCORE:
    print("your grade is D")
elif score >= F_SCORE:
    print('your grade is E')
else:
    print("Failed")
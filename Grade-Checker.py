# Grade Checker
name =  str(input("What is your name: "))
score = int(input("What is your Score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
elif score >= 50:
    grade = "E"
else:
    grade = "F"

if score > 100:
    response = f"Sorry {name}, That's an invalid score"
else:
    response = f"Thanks {name}, Your grade is: {grade}"

print(response)

# 1.  Check if a number is positive and even.

print("1. Check if a number is positive and even.")
num = 5

print("num =", num)
if num > 0 and num % 2 == 0:
    print("Number is positive and even")
else:
    print("number is not positive and even")

# 2.  Check if a person is eligible to vote (age >= 8) and is a citizen.

print("2. Check if a person is eligible to vote (age >= 18) and is a citizen.")

age = 29
citizen = "yes"

print("age =", age)
print("citizen =", citizen)

if age >= 18 and citizen == "yes":
    print("The person is eligible to vote")
else:
    print("The person is not eligible to vote")

# 3.  Check if a number is less than 0 or greater than 00.

print(" 3. Check if a number is less than 0 or greater than 100.")

number = 10
print("number =", 10)

if number < 0:
    print("The number is less than 0")
elif number > 100:
    print("The number is greater than 100")
else:
    print("The number is more than 0 but lesser than 100")

# 4.  Write a program that checks if a student passed (marks ≥ 40) and did not cheat.

print(" 4.  Write a program that checks if a student passed (marks ≥ 40) and did not cheat.")

marks = 40
cheat = "no"

print("marks =", marks)
print("cheat =", cheat)

if marks >= 40 and cheat == "no":
    print("The student passed and did not cheat")
else:
    print("The student failed or cheated")

# 5.  Use `not` to reverse a boolean condition.

print(" 5. Use `not` to reverse a boolean condition.")

number = -9
print("number =", number)

if not (number > 0):
    print("not(number > 0) =", not(number > 0))
else:
    print("Not valid number")

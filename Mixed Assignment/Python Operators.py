# 1. Input the student's:
# a. Name
# b. Marks in 3 subjects (out of 100)
from numpy.ma.extras import average

print("------- Input Fields -------")
name = input("Enter Student's name:")
mark_1 = float(input("Enter English marks: "))
mark_2 = float(input("Enter Bangla marks: "))
mark_3 = float(input("Enter Maths marks: "))
marks = (mark_1,mark_2,mark_3)

# 2. Calculate:
# a. Total marks
# b. Average
# c. Percentage

print("Total: ", sum(marks),  "/100")
print("Average: ", (sum(marks)/len(marks)))
print("Percentage: ", (sum(marks)/300)*100)

# 3.  Assign Grade:
# a. A: 80 and above
# b. B: 70–79
# c. C: 50–69
# d. F: Below 50

grade_point = (sum(marks)/300)*100

if grade_point >= 80:
    print("Grade: A")
elif 70 <= grade_point <= 79:
    print("Grade: B")
elif 50 <= grade_point <= 69:
    print("Grade: C")
else:
    print("Grade: F")

# 4. Use logical and comparison operators to:
# a. Check if the student passed (all subjects ≥ 40)

passed = mark_1>=40 and mark_2>=40 and mark_3>=40

# b. Check if the student is eligible for scholarship (avg ≥ 85 and no subject below 80)

avg = (sum(marks)/len(marks))
scholarship = avg>=85 and mark_1>=80 and mark_2>=80 and mark_3>=80

# 5. Update student record using assignment operators:
# a. Add a bonus of 5 marks to each subject using `+=`

mark_1 += 3
mark_2 += 3
mark_3 += 3

# b. Recalculate total and average after bonus
new_marks = [mark_1,mark_2,mark_3]

Total: sum(new_marks)
Average: sum(new_marks)/len(new_marks)

# 6. Print a full report.
print("------- Student Report -------")

print("Name of the Student: ", name)
print("Marks Obtained: ")
print("English : ", mark_1, "/100")
print("Bangla : ", mark_2, "/100")
print("Maths : ", mark_3, "/100")
print("Total: ", sum(marks),  "/100")
print("Average: ", (sum(marks)/len(marks)))
print("Percentage: ", (sum(marks)/300)*100)
print("Status: PASS" if passed else "Status: FAIL")
print("Eligible for Scholarship" if scholarship else "Not Eligible for Scholarship")
print("Bonus Marks: ")
print("Total: ", sum(new_marks),  "/100")
print("Average: ", (sum(new_marks)/len(new_marks)))









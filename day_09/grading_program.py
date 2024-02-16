students_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

# This is the scoreing criteria:
'''
Scores 91 - 100: Grade = "Outstanding"
Scores 81 - 90: Grade = "Exceeds Expectations"
Scores 71 - 80: Grade = "Acceptable"
Scores 70 or lower: Grade = "Fail"
'''

#TODO-1: Create an empty dictionary called student_grades

students_grades = {}

#TODO-2: Write your code below to add the grades

for student in students_scores:
    if students_scores[student] > 90 and students_scores[student] <= 100:
        students_grades[student] = "Grade = Outstanding"
    elif students_scores[student] > 80:
        students_grades[student] = "Grade = Exceeds Expectations"
    elif students_scores[student] > 70:
        students_grades[student] = "Grade = Acceptable"
    elif students_scores[student] <= 70:
        students_grades[student] = "Grade = Fail"
    else:
        print("Worng number.")
        
print(students_grades)

# Angela's solution
'''for student in students_scores:
    score = students_scores[student]
    if score > 90:
        students_grades[student] = "Outsanding"
    elif score > 80:
        students_grades[student] = "Exceeds Expectations"
    elif score > 70:
        students_grades[student] = "Acceptable"
    else:
        students_grades[student] = "Fail"

print(students_grades)'''

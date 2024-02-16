student_scores = input("Input a list of student heights: ").split()
# 78 65 89 86 55 91 64 89
# Find out the highest score of the students without using max() and min() functions

#Angela's solution
for n in range (0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

print(student_scores)


highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")

''' My solution
aux = 0
max_score = 0

for score in student_scores:
    aux = int(score)
    if max_score < aux:
        max_score = aux
    else:
        max_score = max_score

print(f"The highest score in the class is: {max_score}")'''
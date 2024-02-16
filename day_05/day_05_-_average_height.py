#students_height = [180, 124, 165, 173, 189, 169, 146] 156 178 165 171 187
students_height = input("Input a list of student heights: ").split()

# Angela's solution

# My solution without use len() and sum()
sum = 0
total_students = 0
for height in students_height:
    sum += int(height)
    total_students += 1

average_height = sum / total_students
print(f"The height average is: {round(average_height)}")

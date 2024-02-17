class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def study(self):
        print(f"El estudiante {self.name} esta estudiando.")


user_name = input("Write your name: ")
user_age = input("Write your age: ")
user_grade = input("Write your grade: ")


first_student = Student(user_name, user_age, user_grade)

correct_answer = True
while correct_answer:
    answer = input("What do you want the student does?: ")
    if answer.lower() == "study":
        first_student.study()
        correct_answer = False


print("***Successful student creation***")
print(f"Name: {first_student.name}")
print(f"Age: {first_student.age}")
print(f"Grade: {first_student.grade}")

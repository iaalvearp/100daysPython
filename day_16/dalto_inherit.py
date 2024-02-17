# Simple Inherit Example
class Persona:
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality


class Student():
    def __init__(self, grade, study_method):
        self.grade = grade
        self.study_method = study_method


# Multiple Inherit Example
class TeacherHelper(Persona, Student):
    def __init__(self, name, age, nationality, grade, study_method, payment, subject):
        Persona.__init__(self, name, age, nationality)
        Student.__init__(self, grade, study_method)
        self.payment = payment
        self.subject = subject

    def study(self):
        print(f"{self.name} is studying.")


new_student = TeacherHelper("Roberto", 15, "Ecuadorian", 2, "in_person", 1200, "History")

print(f"""
***Student Register Successful***
Name: {new_student.name}
Age: {new_student.age}
Grade: {new_student.grade}
Method: {new_student.study_method}
Nationality: {new_student.nationality}
Payment: {new_student.payment}
Class: {new_student.subject}
""")

new_student.study()

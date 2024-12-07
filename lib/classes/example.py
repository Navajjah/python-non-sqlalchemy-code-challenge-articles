# def deco(func):
#     def wrapper():
#         print('I wanna sleep')
#         func()
#     return wrapper

# @deco
# def grumble():
#     print('I would like a snack')

# grumble()
class Student:

    all = []

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # teacher is protected because it is not a part of the constructor
        self._teacher = None
        Student.all.append(self)

    @property
    def teacher(self):
        return self._teacher

    @teacher.setter
    def teacher(self, value):
        if not isinstance(value, Teacher):
            raise TypeError("Teacher must be an instance of Teacher class")
        self._teacher = value

class Teacher:
    def __init__(self, name):
        self.name = name

    def students(self):
        return [student for student in Student.all if student.teacher == self]

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Student must be an instance of Student class")
        student.teacher = self

# Create some teachers and students
teacher_1 = Teacher("Mr. Smith")
student_1 = Student("Alice", 12)
student_2 = Student("Bob", 13)

# Add students to the teacher
teacher_1.add_student(student_1)
teacher_1.add_student(student_2)

# Check the teacher of a student
print(student_1.teacher.name)  # Output: Mr. Smith

# Get all students of a teacher
for student in teacher_1.students():
    print(f"Hey i'm {student.name}, in {student.teacher.name}\'s class")  
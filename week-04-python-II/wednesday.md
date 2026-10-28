__init__, initializing method in class
methods get overriden by parent classes from child classes

worked example:
class Student:
    def __init__(self, name, age,grade=0):
        self.name = name
        self.age = age
        if grade < 0 or grade > 100:
            raise ValueError("Grade must be between 0 and 100.")
        else:
            self.grade = grade
    def __str__(self):
        return f"Student(name={self.name}, age={self.age}, grade={self.grade})"
    def set_grade(self, grade):
        self.grade = grade
    def get_grade(self):
        return self.grade 
    def passed(self):
        return self.grade >= 60
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

class StudentClass(Student):
    def __init__(self, name, age, grade=0, class_name=""):
        super().__init__(name, age, grade)
        self.class_name = class_name
    def __str__(self):
        return f"StudentClass(name={self.name}, age={self.age}, grade={self.grade}, class_name={self.class_name})"
    
print("Creating a student object...")
student1 = Student("Alice", 20,100)
student1.greet()
print(f"{student1.passed()}")

print(Student("Alice", 20,100))
print(StudentClass("Alice", 20,100, "Math 101"))


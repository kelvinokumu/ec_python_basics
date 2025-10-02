class Student:
    def __init__(self, name = "Unknown", grade = 0):
        self.name = name
        self.grade = grade

s1 = Student("Alice", 90)
s2 = Student()   # Uses default values

print(s1.name, s1.grade)  # Alice 90
print(s2.name, s2.grade)  # Unknown 0

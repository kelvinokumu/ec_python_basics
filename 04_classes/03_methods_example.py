class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + ' is '  +str(self.age)

    def __repr__(self):
        return  f"Person(name = {self.name}, age = {self.age})"

    def birthday(self):
        print("Happy birthday you were", self.age)
        self.age += 1
        print("You are now", self.age)


p1 = Person("John", 36)
print(p1)
print(p1.birthday())


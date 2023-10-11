class Person: 
    def  __init__(self, name, age):
        self.name = name
        self.age = age
    def greeting(self):
        print(f"Good morning, {self.name}, welcome to the our restaurant, we know that you are {self.age} years old!")

a = Person("John",3)
a.greeting()

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name,age)
        self.student_id = student_id
    def greeting(self):
        super().greeting(self)
        print(f"Good morning, {self.name}, welcome to the our restaurant, we know that you are {self.age} years old and your id is {self.student_id}.")

a = Student("Bob", 13, 134567)

a.greeting
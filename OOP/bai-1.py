#Tạo một lớp Person với các thuộc tính name, age, và phương thức greet().
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello {self.name}, Age is {self.age}")
call = Person("Nhung", 30)
call.greet()

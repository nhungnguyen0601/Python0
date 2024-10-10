#Tạo một lớp Person với các thuộc tính name, age, và phương thức greet().
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello {self.name}, Age is {self.age}")
# call = Person("Nhung", 30)
# call.greet()

#Tạo lớp Student kế thừa từ Person và có thêm thuộc tính grade và phương thức study().
class Student():
    def __init__(self, name, age, grade):
        # super().__init__(name, age)
        self.name = name
        self.age = age
        self.grade = grade

    def study(self):
        print(f"Hoc sinh ten: {self.name}, Tuoi: {self.age}, co diem thi: {self.grade}")
#Tạo một đối tượng Student và gọi các phương thức từ cả lớp cha và lớp con.
student1 = Student("Nhung", 30, 9) 
# student1.greet()
student1.study()


        

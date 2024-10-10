# #Tạo lớp Student kế thừa từ Person và có thêm thuộc tính grade và phương thức study().
# import 
# class Student(bai-1.Person)
from bai import Person
class Studenta(Person):
    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self.grade = grade

# class Student:
#     collage = "kkc"
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#     def hello(self):
#         print("welcom",self.name)

# s1 = Student("arman",99)
# print(s1.name,s1.marks , s1.collage)
# s1.hello()

# class car :
#     color = "blue"
#     brand = "toyota"

# car1 = car()
# print(car1.color)
# print(car1.brand)


# ------------------------------------------------------------------------------
class Student:
    def __init__(self,name , sub1,sub2,sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3
    def avg (self):
        avrage = (self.sub1+self.sub2+self.sub3)/3
        print(f"student name is {self.name} and his avrage marks is {avrage} ")
    @staticmethod
    def hello():
        print("hello students")

obj = Student("arman",60,70,75)
obj.avg()
obj.hello()

# obj1 = Student("arman",0,70,75)
# obj1.avg()
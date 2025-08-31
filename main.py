# print("helo i am arman ,and i am learning python") 

#comment in python using hash symbol

# variyebale---------------
# name = "arman"
# print(name)


# naming convention-------------------
# CamelCase = "thisIsCamelCase"
# PascalCase = "ThisIsPascalCase"
# snake_case = "this_is_snake_case"

# data types ------------------------

# string-----------------

# str = "arman"
# print(type(string))

# number--------------------

# number = 10
# print(type(number))

# floatNumber = 10.5
# print(type(floatNumber))

# complexNumber = 10 + 5j
# print(type(complexNumber))


# boolean-----------------

# isTrue = True
# print(type(isTrue))

# isFalse = False
# print(type(isFalse))

# ---------------------- Input and Output ----------------------

# name = input("Enter your name: ")
# # print("Hello, " + name + "! Welcome to Python programming.")
# print(f"Hello, {name}! Welcome to Python programming.")



# ----------------string and type conversion----------------

# Unicode+++++

# char = "H"
# print(ord(char))

# unicode = 73
# print(chr(unicode))

# string = "arman dhuka"
#  print(string[0]) 
# print(string[0:6:1]) 
# print(string[0::1]) 
# print(string[0::3]) 
# print(string[::-1])  # Reverse the string

# typeConversion =======
# Python automatically converts types when needed, but you can also explicitly convert types using built-in functions.
# For example, to convert a string to an integer, you can use the int() function.
# To convert a string to a float, you can use the float() function.
# To convert a number to a string, you can use the str() function.
# To convert a boolean to a string, you can use the str() function.
# To convert a string to a boolean, you can use the bool() function.


# Example of type conversion:

# string = "10"
# print(type(string)) 
# number = int(string)
# print(type(number)) 

# floatNumber = 10.5
# print(type(floatNumber))
# number = int(floatNumber)
# print(type(number))


# What are operators in Python?

# Operators are special symbols that perform operations on variables and values.
# Python has many types of operators, including arithmetic operators, comparison operators, logical operators, assignment operators, and more.

# Arithmetic Operators
# Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, and division.

# Example of arithmetic operators:

# a=10
# b=5
# print(a + b)  # Addition
# print(a - b)  # Subtraction
# print(a * b)  # Multiplication
# print(a / b)  # Division
# print(a % b)  # Modulus (remainder)
# print(a ** b)  # Exponentiation (a raised to the power of b)
# print(a // b)  # Floor division (quotient without remainder)


# Example assingnment Operators

# Assignment operators are used to assign a value to a variable.
# a = 10
# b = 5

# a += b  # Equivalent to a = a + b
# print(a)  # Output: 15

# b -= 2  # Equivalent to b = b - 2
# print(b)  # Output: 3

# a *= b  # Equivalent to a = a * b
# print(a)  # Output: 45

# b /= 2  # Equivalent to b = b / 2
# print(b)  # Output: 1.5

# a %= b  # Equivalent to a = a % b
# print(a)  # Output: 0.0

# b **= 2  # Equivalent to b = b ** 2
# print(b)  # Output: 2.25

# b //= 2  # Equivalent to b = b // 2
# print(b)  # Output: 1.0


# Comparison Operators
# Comparison operators are used to compare two values and return a boolean result (True or False).

# Example of comparison operators:

# a = 10
# b = 5
# print(a == b)  # Equal to
# print(a != b)  # Not equal to
# print(a > b)   # Greater than
# print(a < b)   # Less than
# print(a >= b)  # Greater than or equal to
# print(a <= b)  # Less than or equal to


# Logical Operators
# Logical operators are used to combine conditional statements and return a boolean result.

# Example of logical operators:
# a = True
# b = False
# print(a and b)  # Logical AND
# print(a or b)   # Logical OR
# print(not a)    # Logical NOT

# ---------------------conditional statement----------------

# mony = 30

# if mony < 10 :
#     print("i have note a avelibale mony")

# elif mony <= 20 :
#     print("i can shopping under 20 ")

# else :
#      print("i can buy under 30")


# ----------------------loops in python ------------------

# only two type of loop in python
# for loop 
# while loop

# for loop in number

# a = range(1,11,1)

# for i in a :
#     print(i)

# r = range(11,0,-1)

# for i in r :
#     print(i)


# loop in string_____________________________________________

# using indexing_________

# str = "arman dhuka"

# for i in range(len(str)):
#     print(str[i])


# using direct

# str = "all guy is cool"
# for i in str:
#     print(i)


# ------------------------break and continue ------------------

# for i in range(10):
#     if i == 6:
#         continue
#     print(i)


# for i in range(10):
#     if i == 6:
#         break
#     print(i)



# --------------------- while loop --------------------

# a = 2567

# while a > 0:
#     print(a%10)
#     a = a // 10

# ___________________________ Function in python ____________________

# def sum(a=1,b=1):
#     return (f"{a} + {b} = {a+b}")

# print(sum(10,12))
# print(sum(10))
# print(sum(b=22,a=12))


# ___________list___________________

# a=[1,2,"arman",8,34,]
# a.append("hello")
# a.insert(2,"me hu baba tillu")
# print(a)

# for i in range(len(a)):
#     print(a[i])

# for i in a:
#     print(i)


# ---------------tuple-----------------------

# a = (1,2,3,4,5,6)

# for i in a:
#     print(i)

# for i in range(len(a)):
#     print(a[i])


# a,b,c,d = (1,2,3,4)
# print(a,b,c,d)

# a = (1,)
# print(type(a))


# -------------------- set ------------------------

# ✅ Set kya hota hai?

# Ek mutable (change kar sakte ho) data type hai.

# Har element unique hota hai (duplicate values automatically remove ho jaati hain).

# Unordered hota hai (indexing nahi hoti).

# Curly braces {} me likhte hain ya set() constructor use karte hain.

# Example of set:**************
# a = {1,2,3,4,5}

# No duplicates**************

# num = {1, 2, 3, 4, 5, 1, 2}
# print(num)

# Add element****************

# s = {1, 2, 3}
# s.add(4)
# print(s)  # Output: {1, 2, 3, 4}

# Remove element****************

# s = {1, 2, 3, 4}
# s.remove(2)
# print(s)  # Output: {1, 3, 4}


# Pop (random element remove karta hai)*************

# s.pop()

# Clear

# s.clear()  # Empty kar dega


# 🛠 Set Operations (Math ke jaise)***********

# Union (|) → Combine(sab elements ko mila deta hai)

# a = {1, 2, 3}
# b = {3, 4, 5}
# print(a | b)  # {1, 2, 3, 4, 5}


# Intersection (&) → Common elements (dono me jo common hai)

# print(a & b)  # {3}


# Difference (-) → Jo first me hai, second me nahi (first set se second set ko subtract karta hai)

# print(a - b)  # {1, 2}


# Symmetric Difference (^) → Jo dono me common nahi (unique elements dono sets me)

# print(a ^ b)  # {1, 2, 4, 5}


# --------------------- Dictionary ----------------------

# Dictionary kya hota hai?
# Ek mutable (change kar sakte ho) data type hai.
# Key-value pairs me data store karta hai.
# Keys unique hoti hain, values duplicate ho sakti hain.

# Example of dictionary:
# student = {
#     "name": "Arman",
#     "age": 20,
#     "city": "Delhi"
# }

# Accessing values:

# print(student["name"])  # Output: Arman

# Adding a new key-value pair:

# student["grade"] = "A"
# print(student)  # Output: {'name': 'Arman', 'age': 20, 'city': 'Delhi', 'grade': 'A'}

# Removing a key-value pair:
# student.pop("age") / delete student["age"]
# print(student)  # Output: {'name': 'Arman', 'city': 'Delhi', 'grade': 'A'}

# Iterating through a dictionary:

# for key, value in student.items():
#     print(f"{key}: {value}")


# a = { 1:100, 2:200, 3:300, 4:400 }

# for i in a:
#     print(f"{i} and {a[i]} ")

# a = { 1:100, 2:200, 3:300, 4:400 }

# for i in a.values():
#     print(i)

# print(a.items())

# help(dict)


#---------------------- Exception Handling----------------

# a = int(input("enter a number"))

# try:
#     print(10/a)
# except Exception as err:
#     print(err)
# else:
#     print("no err find")

# finally :
#     print("i will run no matter what")

# print("i have completed my work")

# b = int(input("enter your age :- "))
# try:
#     if b<10 or b>18:
#         raise ageErr("your age is no selected")
#     else :
#         print("welcom to the club")
# except Exception as err:
#     print(f"an err occured as {err}")

# print("the club will start soon")


# ------------------ file handling ---------------

# r = open('main.py')
# print(r.read())

# r=open("super.txt",'w')
# r.write("hello my name is arman dhuka")
# r.close()

# r=open("super.txt",'a')
# r.write("and this content is appendin, i am from palanpur")
# r.close()

# r=open("supera.txt",'x')
# r.write("and this content is appendin, i am from palanpur")
# r.close()


# ------------------ oops ---------------------

# class Factory:
#     a = 12

#     def hello(self):
#         print("hello i am arman dhuka")
#     print("hello i am arman dhuka from factory class")

# print(Factory.a)
# Factory().hello()


# Constructor====

# class Factory:
#     def __init__(self,mete,zips,pockets):
#         self.mete = mete
#         self.zips = zips
#         self.pockets = pockets

#     def show(self):
#         print(f"Material: {self.mete}, Zips: {self.zips}, Pockets: {self.pockets}")


# reebok = Factory("leather",2,4)
# campus = Factory("leather",2,4)
# print(reebok.pockets,campus.pockets)

# reebok.show()

# type of Attributes and Methods:===========

# class animal :
#     name = "dog" # class attribute
#     def __init__(self,age): # instance attribute
#         self.age = age

#     def show(self): # instance method
#         print(f"The animal is a {self.name} and its age is {self.age} years.")

#     @classmethod
#     def hello(cls):
#         print(f"Hello, I am a {cls.name} from the animal class.")
#     @staticmethod
#     def static_method():
#         print("This is a static method that doesn't depend on class or instance")

# obj = animal(5)
# obj.show()
# obj.hello()
# obj.static_method()


# ------------------ inheritance ---------------------
# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def show(self):
#         print(f"The animal is a {self.name}.")

# class Dog(Animal):
#     def __init__(self, name,age):
#         super().__init__(name)
#         self.age = age

#     def show(self):
#         print(f"The dog is a {self.name} and its age is {self.age} years.")

# Animal = Animal("Lion")
# Dog = Dog("Dog", 5)

# Animal.show()
# Dog.show()


# multiple inheritance =============

# class animal:
#     name1 = "dog"

# class human:
#     name2 = "arman"

# class robot (animal,human):
#     nameRobo = 'char3'


# obj = robot()
# print(obj.name2)

# multileval inheritance============

# class Fectory:
#     def __init__(self,meterial,zips):
#         self.meterial = meterial
#         self.zips = zips

# class FectoryPune(Fectory):
#     def __init__(self, meterial, zips,color):
#         super().__init__(meterial, zips)
#         self.color = color

# class FectoryGuj(FectoryPune):
#     def __init__(self, meterial, zips, color,pocket):
#         super().__init__(meterial, zips, color)
#         self.pocket = pocket


# ===============pholymorphism================

# ======================================dunder method========================================

# class animal :
#     def __init__(self,name):
#         self.name = name
#     def __dir__(self):
#         return f"hello i am a {self.name}"
    
# obj = animal("cat")
# print(obj.__dir__())


# ============================== decorater ========================

# def decorator_function(original_function):
#     def wrapper_function():
#         print("Wrapper executed before")
#         original_function()
#         print("Wrapper executed affter")
       
#     return wrapper_function

# @decorator_function
# def original_function():
#     print("i am original fuction")

# original_function()

# ========================== args(*) and kwarges(**) ===================================

# def add(*args):
#     sum = 0
#     for i in args:
#         sum += i
#     return sum

# print(add(12,32,4,34,2,22,34,12))


# def info (**kwargs):
#     print("your info is \n")
#     for i in kwargs:
#         print(f"{i}:{kwargs[i]}")
# info(name="arman",age=17,profetion="ai ml")


# ================================= ternory,comprehencive, list desctory =========================

# num = 13 
# if num % 2==0 : print("even") 
# else : print("odd")

# list = [ i for i in range(1,11) if i]
# print(list)

# deco = {i:i*2 for i in range(1,11) if i}
# print(deco)

# set = (i for i in range(1,11) if i)
# print(set)

# add = lambda a,b : a+b
# print(add(10,12))

# ============================== map & filter =========================


# a = [1,2,3,4,5]
# def dbl(x):
#     return x *2
# resut = map(dbl,a)
# print(list(resut))

# a = [1,2,3,4,5]
# result = map(lambda X : X*2,a)
# print(list(result))

a = [1,2,3,4,5]

result = filter(lambda x: x % 2 == 0, a)
print(list(result))
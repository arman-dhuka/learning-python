# 1️⃣ Variables & Naming Conventions

# Easy:
# Store your name in a variable and print it.

# myName = "arman"
# print(myName)

# Medium:
# 2. Store your name, age, and city in three variables, then print them in one line using an f-string.

# myName = "arman"
# myAge = "17"
# myCity = "Palanpur"
# print(f"hello my name is {myName},and my age is {myAge} ,and i am from {myCity}")

# Hard:
# 3. Store two numbers in variables, create a third variable that stores their sum, and print all values in a formatted sentence.

# num1 = 10
# num2 = 7
# sum = num1+num2
# print(sum)



# 2️⃣ Data Types (string, int, float, bool)
# Easy:
# Store "123" as a string, convert it to an integer, and multiply it by 10.

# str = "123"
# integer = int(str)
# print(integer*10)

# Medium:
# 2. Convert a float number into an integer and print both values.
# flot = 10.14
# int = int(flot)
# print(flot,int)

# Hard:
# 3. Convert a boolean value into a string and print its type.
# isTrue = True
# print(type(isTrue))
# str = str(isTrue)
# print(type(str))




# 4️⃣ String & Type Conversion
# Easy:
# Reverse the string "Python".
# str = "Python"
# print(str[::-1])

# Medium:
# 2. From "Hello World", print only "World" using slicing.
# word = "Hello World"
# print(word[6::1])

# Hard:
# 3. Count how many vowels (a, e, i, o, u) are in a sentence and print the result.

# 5️⃣ Arithmetic Operators
# Easy:

# Print the sum, difference, multiplication, and division of two numbers.

# a = 10
# b = 20
# print(f"{a}+{b}={a+b}")
# print(f"{a}-{b}={a-b}")
# print(f"{a}*{b}={a*b}")
# print(f"{a}/{b}={a/b}")



# Medium:
# 2. Take a number from the user and print its square and cube.

# Hard:
# 3. Find the largest among three numbers without using the built-in max() function.

# 6️⃣ Assignment Operators
# Easy:

# Store 5 in a variable, apply += 2, then *= 3, and print the final value.
# num = 5
# num += 2
# num *=3
# print(num)

# Medium:
# 2. Store 100 in a variable, apply -= 20, then /= 4, and print the result.
# num = 100
# num -=20
# num /=4
# print(num)

# Hard:
# 3. Store 7 in a variable and use each assignment operator (+=, -=, *=, /=, %=) at least once to print different results.

# 7️⃣ Comparison Operators
# Easy:
# Compare two numbers and print whether they are equal.
# print(10==10)

# Medium:
# 2. Take age as input and check if it’s greater than 18.
# age = int (input("enter your age"))
# print(age >= 18)

# Hard:
# 3. Take three numbers and check if the first is greater than the second and less than the third.

# 8️⃣ Logical Operators
# Easy:

# Create two boolean variables and print the result of and, or, and not operations.

# Medium:
# 2. Take two numbers as input and check if both are even using logical operators.

# Hard:
# 3. Take age and country as input:

# If age ≥ 18 and country is "India", print "Eligible for voting".

# Otherwise, print "Not eligible".

# 🔥 Extra 3 Mixed Questions (Everything Combined)
# Take a number from the user.

# If it’s even, reverse the string "Python".

# If it’s odd, print the square of the number.

# Take a sentence as input, count the number of vowels in it, and print whether the count is greater than 5 or not.

# Ask the user for two numbers and:

# Print their sum.

# Check if the sum is divisible by 3.

# If it is, print "Divisible by 3", else "Not divisible by 3".




# -------------------------------------------------------------------------------------------------------
# Accept two numbers and print the greatest between them ----------------

# num1 = int(input("plesae tell me a num 1 "))
# num2 = int(input("plesae tell me a num 2 "))

# if num1 > num2 :
#     print(f"{num1} is greter then {num2}")

# elif num1 == num2 :
#     print(f"{num1} and {num2} both are equal")

# else :
#     print(f"{num2} is greter then {num1}")


# accsept the gender and give a greeting--------
# gen = input("enter the gender :- ")

# if gen == "male" :
#     print("good morning sir")
# elif gen == "female":
#     print("good morning mam")
# else :
#     print(f"good morning {gen}")

# even or odd  ------------

# num = int(input("enter a number :- "))

# if num%2==0 :
#     print(f"{num} is even")

# else :
#     print(f"{num} is odd")


# valid voter cheker----------

# name = input("plz tell me your name :-")
# age = int(input("plz tell me your age :-"))

# if age >= 18 :
#     print(f"hello {name} you are aligeble to vote ")

# else :
#     print(f"hello {name} you are not aligeble to vote ")


# leep years ------------------------

# year = int(input("give me a one years :- "))

# if (year%4==0 and year%100 !=0) or year%400==0 :
#     print (f"{year} is leep years")

# else :
#     print (f"{year} is not leep years")


# tempreture----------------------------

# temp = int(input("plz tell me a temptrue"))

# if temp < 0 :
#     print("freezing cold") 
# elif temp <= 10 :
#     print("very cold") 
# elif temp <= 20 :
#     print("cold") 
# elif temp <= 30 :
#     print("pleasent") 
# elif temp <= 40 :
#     print("hote") 
# else :
#     print(" very hote") 


# ----------------------------loop--------------------------------------
# print teable of 5

# ____________________________________
# for i in range (1,11,1):            |
    # print(f"5 * {i} = {i*5}")       |
                                  #   |
# for i in range (5,51,5):            |       
    # print(i)                        |
# ____________________________________|


# # print n time _____

# n = int(input("enter a one number"))

# for i in range(n):
#     print(f"{i+1} Hello word")


# n number print__________

# a = int(input("give me a number :- "))

# for i in range(1,a+1):
#     print(i)

# reverce n number print__________

# n = int(input("give me a number :- "))

# for i in range(n,0,-1):
#     print(i)


# sum n number _______________

# sum = 0
# n = int(input("enter a number :- "))

# for i in range(1 ,n+1):
#      sum = sum + i

# print(sum)

# factorial number________________

# num = int(input("enter a number :- "))
# fac = 1
# for i in range(2,num+1):
#     fac *= i

# print(fac)


# print the sum of all even and odd number in a given range___________

# n = int(input("enter a number :- "))
# even = 0
# odd = 0
# for i in range(1,n+1):
#     if i%2==0 :
#         even += i
#     else :
#         odd +=i

# print(even,odd)


# n number factor ____________

# n = int(input("enter a number :- "))

# for i in range(1,n+1):
#     if n%i==0:
#         print(i)

# get a perfect number__________

# n = int(input("enter a number :- "))
# p=0
# for i in range(1,n):
#     if n%i==0:
#         p += i
           
# if p == n :
#     print(f"{n} is perfect")
# else :
#     print(f"{n} is not perfect")


# is prime cheker

# n = int(input("enter a number :- "))
# p=0
# for i in range(1,n+1):
#     if n%i==0:
#         p = p+1

# print(p)

# if p == 2:
#     print("num is prime")
# else :
#     print("num is not prime")


# reverce a string without usin in build fuction using foor loop_________________________

# name = "Arman Dhuka"
# rev = ''

# for i in range(len(name)-1,-1,-1):
#     rev += name[i]

# print(rev)


# pelindrom chekar_________________________

# name = input("enter a name :- ")
# rev = ""
# for i in range(len(name)-1,-1,-1):
#     rev += name[i]

# if name == rev :
#     print(f"{name} is pelindrom")
# else :
#     print(f"{name} is not pelindrom")

# ---------------------------

# n=input("enter a paregraph :- ")

# digit = 0
# schar = 0
# alpha = 0

# for i in n:
#     if i.isdigit():
#         digit += 1
#     elif i.isalpha():
#         alpha += 1
#     else :
#         schar += 1

# print(f"digit is {digit} , special cherecter is {schar},alphabets is {alpha}")


# ------------while loop------------

# a = int(input("tell me a number :- "))
# rev = 0
# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10

# print(rev)

# chek a pelindrom using while loop___________________

# a = int(input("tell me a number :- "))
# copy = a
# rev = 0
# while a > 0:
#     rev = rev * 10 + a % 10
#     a = a // 10

# if copy == rev : 
#     print("it is pelindron")
# else :
#     print("it is not pelindron")


# _________________________list______________________________

# print a positive and negetive value--------------------------------

# a =[ 1,2,-32,34,-23,-1,34.5,]

# print("positive numbr")
# for i in a:
#     if i > 0 :
#         print(i)
# print("negetive numbr")
# for i in a:
#     if i < 0 :
#         print(i)


# mean of avrage number--------------------------

# a = [1,2,3,4,5,12,23,21]
# sum=0
# for i in a :
#     sum += i

# print(sum/len(a))

# accses the grethest elment and smallest element---------------------

# a = [10,20,5,234,23,54,340,65,76,23]
# g=a[0]
# l=a[0]
# for i in a:
#     if g < i :
#         g = i 
#     elif l>i:
#         l = i

# print(g,"this is a gretest elem")
# print(l,"this is the smallest elem")

# finde a second smalest and gretest  element----------------

# a = [10,20,5,234,23,54,340,65,76,23,339]
# largest = a[0]
# s_largest = a[0]
# for i in a:
#     if i > largest :
#         s_largest = largest
#         largest = i
#     elif i > s_largest and i != largest:
#         s_largest = i

# print(largest,s_largest)


# chek if list is sorted or not-----------------------

# lst = [4,3,2,1]
# lst = [1,2,3,4]
# is_desending = True
# is_ascending = True

# for i in range(len(lst)-1) :
#     if lst[i] < lst[i+1]:
#         is_desending = False
#     elif lst[i] > lst[i+1]:
#         is_ascending = False

# if is_desending :
#     print("list is sort in desending order")
# elif is_ascending :
#     print("list is sort in asending order")
# else:
#     print("note sorted")


# ====================================================================================================
# ✅ Simple Questions

# Reverse a String ---------------
# Take a string input from the user and print it in reverse without using any built-in reverse function.

# str = input("enter a string:- ")
# rev= ""
# for i in range(len(str)-1,-1,-1):
#     rev += str[i]

# print(rev)

# Check Even or Odd-----------
# Ask the user to enter a number and print whether it is even or odd using an if-else condition.

# num = int(input("enter a number"))

# if num%2==0 : 
#     print("num is odd")
# else:
#     print("num is even")

# ✅ Medium Questions

# Sum of Digits
# Take an integer input from the user and print the sum of its digits using a while loop.

# num = int(input("enter a number :- "))
# sum = 0
# while num > 0 :
#     sum += num%10
#     num//=10
# print(sum)

# Count Vowels and Consonants-----------------------------
# Take a string input and count how many vowels and consonants it contains.

# text = input("Enter a string: ")

# vowels = 0
# consonants = 0
# vowel_set = "aeiou"

# for i in text.lower():
#     if i.isalpha():
#         if i in vowel_set:
#             vowels +=1
#         else:
#             consonants +=1 

# print(f"Vowels: {vowels}, Consonants: {consonants}")

# ✅ Advanced Question (Mini Project)===========

# Student Management System (Console-based)
# Create a program that:

# Displays a menu:
# 1. Add Student, 2. View Students, 3. Search Student by Name, 4. Exit

# Use a list to store student names.
# students = []

# def add_student():
#     name = input("Enter student name: ")
#     students.append(name)
#     print(f"Student '{name}' added successfully.")

# def view_students():
#     if not students:
#         print("No students found.")
#     else:
#         print("List of Students:")
#         for idx, student in enumerate(students, start=1):
#             print(f"{idx}. {student}")

# def search_student():
#     name = input("Enter student name to search: ")
#     found_students = [student for student in students if name.lower() in student.lower()]
    
#     if found_students:
#         print("Found Students:")
#         for student in found_students:
#             print(student)
#     else:
#         print(f"No students found with the name '{name}'.")

# def main():
#     while True:
#         print("\nMenu:")
#         print("1. Add Student")
#         print("2. View Students")
#         print("3. Search Student by Name")
#         print("4. Exit")
        
#         choice = input("Enter your choice (1-4): ")
        
#         if choice == '1':
#             add_student()
#         elif choice == '2':
#             view_students()
#         elif choice == '3':
#             search_student()
#         elif choice == '4':
#             print("Exiting the program.")
#             break
#         else:
#             print("Invalid choice, please try again.")

# if __name__ == "__main__":
#     main()



# Use functions for each feature.

# Use loops to keep showing the menu until the user exits.

# Handle user input properly.

# Add some string slicing or indexing when showing names.






# ================================================================================================/

# Dictionary **************************

# a = {1:100,2:200,3:300,4:400}
# b = {5:500,6:600,7:700,8:800}

# for i in b:
#     a[i] = b[i]

# print(a)

# sum of the value of dictionary -------------

# a = {1:1,2:2,3:3,4:4}
# sum = 0
# for i in a.values():
#     sum += i

# print(sum)

# chek a friqvincy in a list--------------------

# a = [1,2,1,3,2,2,3,4,2,5,3,3,4]
# d = {}
# for i in a :
#     if i in d.keys():
#         d[i] += 1
#     else:
#         d[i] = 1

# print(d)


# =============================================================================================================

# ✅ Functions (3 Questions)

# Q1 (Easy):
# Write a function greet(name) that prints "Hello, <name>!".
# Example:
# greet("Arman") → Hello, Arman!

# def greet(name):
#     print(f"hello {name}")
# greet("arman dhuka")

# Q2 (Medium):
# Write a function multiply(a=2, b=3) that returns the product of two numbers.
# Test it with:

# def multiply(a=2, b=3):
#     print(a*b)
# multiply(4, 5)
# multiply(10)
# multiply(b=7, a=3)

# Q3 (Advanced):
# Write a function calculate(*args) that takes any number of integers and returns:
# Sum of all numbers
# Maximum number
# Minimum number
# Example:
# calculate(1, 2, 3, 4, 5) → Sum: 15, Max: 5, Min: 1

# def calculate(*args):
#     num = args
#     sum = 0
#     for i in num:
#         sum += i 
    
#     max = args[0]
#     for mx in num:
#         if max < mx:
#             max = mx
#     min = args[0]
#     for mi in num:
#         if min > mi :
#             min = mi
#     print(f"Sum: {sum}, Max: {max}, Min: {min}")

# calculate(1112,32,43,0,2,32,76,54)

# def calculate(*args):
#     if not args:
#         print("not avelibale")
#         return
    
#     total = sum(args)
#     maximum = max(args)
#     minimum = min(args)
#     print(f"Sum: {total}, Max: {maximum}, Min: {minimum}")

# calculate(1112,32,43,0,2,32,76,54)


# ✅ Lists (3 Questions)

# Q1 (Easy):
# Create a list of your 5 favorite fruits. Add "Mango" at the end and print the list.

# fruits = ["apple","banana","orange"]
# fruits.append("mango")
# print(fruits)

# Q2 (Medium):-------------------
# Given a list:
# numbers = [10, 20, 30, 40, 50]
# Write a program to:
# Insert 15 at index 1
# Remove 40
# Print the list in reverse order

# numbers = [10, 20, 30, 40, 50]
# numbers.insert(1,15)
# numbers.remove(40)
# reversed_list = []
# for i in range(len(numbers)-1,-1,-1):
#     reversed_list.append(numbers[i])
# print(reversed_list)

# Q3 (Advanced):--------------------
# Take a list of integers from the user (using input()) and:
# Remove duplicates
# Sort the list in ascending order
# Print the result

# numbers = list(map(int, input("Enter numbers separated by space: ").split()))
# unique_list = sorted(set(numbers))
# print(unique_list)



# ✅ Tuples (3 Questions)

# Q1 (Easy):
# Create a tuple of 4 colors and print each color using a loop.
# colors = ("red", "green", "blue", "yellow")
# for i in colors:
#     print(i)

# Q2 (Medium):
# Write a program to unpack a tuple (10, 20, 30) into three variables and print them.
# a,b,c=(10, 20, 30)
# print(a, b, c)

# Q3 (Advanced):
# Create a tuple of numbers and find:
# Sum of elements
# Maximum element
# Count how many times 2 occurs in the tuple

# numbers = (1, 2, 3, 2, 4, 5, 2)
# sum = sum(numbers)
# maximum = max(numbers)
# count_of_two = numbers.count(2)
# print(f"Sum: {sum}, Max: {maximum}, Count of 2: {count_of_two}")

# ✅ Sets (3 Questions)

# Q1 (Easy):
# Create a set with numbers {1, 2, 3} and:
# Add 4
# Remove 2
# Print the set
# numbers = {1, 2, 3}
# numbers.add(4)
# numbers.remove(2)
# print(numbers)

# Q2 (Medium):
# Given two sets:
# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}
# Print:
# Union
# Intersection
# Difference (A-B)

# A = {1, 2, 3, 4}
# B = {3, 4, 5, 6}

# print("Union:", A|B)
# print("Intersection:", A.intersection(B))      
# print("Difference (A-B):", A-B)

# Q3 (Advanced):
# Write a program that:
# Takes a list with duplicate values
# Converts it into a set (to remove duplicates)
# Converts it back into a sorted list

# numbers = [1, 2, 3, 2, 4, 5, 3]
# unique_numbers = set(numbers)
# sorted_list = sorted(unique_numbers)
# print(sorted_list)

# ✅ Dictionaries (3 Questions)

# Q1 (Easy):
# Create a dictionary with keys: "name", "age", "city". Print each key-value pair.

# Q2 (Medium):
# Create a dictionary of 3 students with their marks (roll number as key). Print only the names of students who scored more than 80.

# Q3 (Advanced):
# Write a program that:

# Takes a sentence from the user

# Counts the frequency of each word

# Stores it in a dictionary and prints it
# Example:
# Input: "hello world hello"
# Output: {'hello': 2, 'world': 1}

# ✅ Mixed Questions (Easy → Advanced)

# Q1 (Easy):
# Write a program to take 5 numbers as input, store them in a list, and print their sum.

# Q2 (Medium):
# Write a program that:

# Takes a list of numbers

# Stores unique numbers in a set

# Prints the largest and smallest number

# Q3 (Advanced):
# Create a Student Management System where:

# Each student is stored as a dictionary with keys: "name", "age", "marks".

# All students are stored in a list.

# Write functions to:

# Add a new student

# Display all students

# Show the student with the highest marks




# =============== CURD ==============

# import os

# def create(filename):
#     try:
#         with open(filename, "x") as f:
#             print(f"File '{filename}' created successfully.")
#     except FileExistsError:
#         print(f"Error: File '{filename}' already exists.")

# def read(filename):
#     try:
#         with open(filename, "r") as f:
#             content = f.read()
#             print("\nFile Content:")
#             print(content)
#     except FileNotFoundError:
#         print(f"Error: File '{filename}' not found.")

# def update(filename, content):
#     try:
#         with open(filename, "a") as f:  # Append mode
#             f.write(content + "\n")
#             print(f"Content added to '{filename}'.")
#     except FileNotFoundError:
#         print(f"Error: File '{filename}' not found.")

# def delete(filename):
#     try:
#         os.remove(filename)
#         print(f"File '{filename}' deleted successfully.")
#     except FileNotFoundError:
#         print(f"Error: File '{filename}' not found.")

# print("Create a file  : 1")
# print("Read a file    : 2")
# print("Update a file  : 3")
# print("Delete a file  : 4")

# inp = int(input("Choose a number (1,2,3,4): "))

# if inp == 1:
#     cr = input("Enter a file name: ")
#     create(cr)
# elif inp == 2:
#     re = input("Enter a file name: ")
#     read(re)
# elif inp == 3:
#     up = input("Enter a file name: ")
#     con = input("Enter content: ")
#     update(up, con)
# elif inp == 4:
#     dl = input("Enter a file name to delete: ")
#     delete(dl)
# else:
#     print("Invalid choice!")

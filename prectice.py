# Data Types (list, tuple, dict, set) aur unke advanced methods

# ✅  LIST (Most Flexible)
# Basic Features
# Ordered (index-based)
# Mutable (change kar sakte ho)
# Duplicates allowed

# Example:
# nums = [10, 20, 30, 20]

# | Method                          | Description                             |
# | ------------------------------- | --------------------------------------- |
# | `append(x)`                     | Last me element add karega              |
# | `insert(i, x)`                  | Specific index pe element insert karega |
# | `extend(iterable)`              | Do list merge karega                    |
# | `remove(x)`                     | Pehla occurrence remove karega          |
# | `pop([i])`                      | Element remove + return karega          |
# | `clear()`                       | Empty list bana dega                    |
# | `index(x)`                      | First index of element                  |
# | `count(x)`                      | Element count karega                    |
# | `sort(key=None, reverse=False)` | Sorting (customizable)                  |
# | `reverse()`                     | List ko reverse karega                  |

# Advanced:
# List comprehension: [x**2 for x in range(10) if x % 2 == 0]
# Slicing: nums[::-1] (reverse list)
# Unpacking: a, *b, c = [1, 2, 3, 4, 5]

# nums = [10, 20, 30, 20]
# nums.append(40)
# nums.insert(2,50)
# nums.extend([60, 70, 80])
# nums.remove(20)
#nums.pop() # Last element remove karega
#nums.clear()  # List ko empty karega
#print(nums.index(20))  # First occurrence of 20 ka index
# print(nums.count(20))  # Count of 20 in the list
# nums.sort(reverse=True)  # Descending order sort
# nums.reverse()  # Reverse the list

# start = 1
# end = 4
# steps = 2
# print(nums[start:end:steps]) # Slicing example
# print(nums)


# *a, b, c = [1, 2, 3, 4, 5]
# print(f"a={a},b={b},c={c}")  


# ==============================================================================
# TUPLE (Immutable List)

# Ordered
# Immutable (change nahi kar sakte)
# Duplicates allowed

# Example:
# t = (10, 20, 30,10,40,10)
# t[1]= 50  # Error: Tuples are immutable

# Important Methods:
# count(x)
# print(t.count(10))  # Count of 10 in the tuple
# index(x)
# print(t.index(20))  # First index of 20 in the tuple

# Packing & Unpacking: a, b, c = (1, 2, 3)

# Why use Tuple?
# Faster than list
# Can be used as dictionary keys
# Safe from modification

# =======================================================================

# 4. SET (Unique Elements)
# Unordered
# Mutable (elements add/remove)
# No duplicates allowed

# Example:

# s = {10, 20,70,50, 30, 40}

# Important Methods

# Method	                                     Description

# add(x)	                            Add element
# update(iterable)	                    Multiple elements add
# remove(x)	                            Element delete (error if not found)
# discard(x)                            Same as remove but no error
# pop()                                	Random element remove
# clear()	                            Empty set


# Set Operations (VERY POWERFUL)

# union() / |
# intersection() / &
# difference() / -
# symmetric_difference() / ^
# issubset(), issuperset()

# Example:
# s.add(40)
# s.update([50, 60,100])
# s.remove(20)  
# s.discard(50) # No error if 50 not found
# s.pop()
# s.clear()  # Empty the set
  
# print(s) 
# 
# ===================================================================================
# 
# 5. DICT (Key-Value Pair)

# Ordered (Python 3.7+)
# Mutable
# Keys unique hote hain

# Example:
# student = {"name": "Raj", "age": 21}
# print(student.items())
# Important Methods
# Method	Description
# get(key, default)	Safe access
# keys()	All keys
# values()	All values
# items()	Key-value pairs
# update()	Merge dict
# pop(key)	Remove key
# popitem()	Last inserted key remove
# setdefault()	Default value set kare

# Advanced

# Dictionary Comprehension:
# squares = {x: x**2 for x in range(5)}

# Nested Dicts for complex data
# Merging dicts (Python 3.9+):

# d1 = {"a": 1}
# d2 = {"b": 2}
# merged = d1 | d2
 

# ===============================================================================
# List comprehensions & dictionary comprehensions

# (a) Simple list comprehension------------
# num = [1,2,3,4,5]
# sqr = [ n**2 for n in num ]
# print(sqr)

# (b) With condition-------------------
# num = [1,2,3,4,5,6]
# even = [n for n in num if n%2==0 ]
# print(even)

# (c) Nested loop comprehension------------
# pairs = [(x,y) for x in range(1,4) for y in range (3,6)]
# print(pairs)

# Advanced Trick: With function----------
# word = ["hello", "world", "python", "rocks"]
# up_word = [w.upper() for w in word ]
# len_word = [len(w) for w in word if len(w) > 4]
# print(up_word,len_word)


# 2. Dictionary Comprehension =====

# (a) Basic dict comprehension-----------
# num = [1,2,3,4,5]
# sqr = { n:n**2 for n in num }
# print(sqr)

# (b) With condition-------------------
# num = [1,2,3,4,5,6]
# even = {n:n**2 for n in num if n%2==0 }
# print(even)

# (c) Key-value swapping-----------
# data = {'a': 1, 'b': 2, 'c': 3}
# sqr = {k:v for v,k in data.items()}
# print(sqr)

# Nested dictionary comprehension
# nast = {i : {j:i*j for j in range(1,3)} for i in range(1,6)}
# print(nast)


# =================================================================================
# Functions (lambda, map, filter, reduce)

# 1. Lambda Functions (Anonymous Functions)
# sqr = lambda x : x**2
# print(sqr(5))

# 2. Map() Function
# num = [1, 2,4, 3, 4, 5]
# sqr = tuple(map(lambda x : x**2 , num))  
# print(sqr)

# 3. filter() Function
# num = [1, 2, 3, 4, 5]
# even = tuple(filter(lambda x : x%2 == 0 , num))  
# print(even)

# 4. reduce() Function
# from functools import reduce
# num = [1, 2, 3, 4, 5]
# product = reduce(lambda x,y : x*y, num)
# print(product)  


# ==================================================================================
# String manipulation (split, join, format, f-string)

# text = "Hello, World! Welcome to Python programming."
# result = text.split(',')
# print(result) 

# text = "Hello, World! Welcome to Python programming."
# result = "-".join(text)
# print(result) 


# name = "Rahul"
# age = 25
# print("My name is {} and I am {} years old.".format(name, age))
# print("{1} is older than {0}".format("Rahul", "Amit"))  # Amit is older than Rahul

# ✔ Input cleaning → strip(), lower(), replace()
# ✔ Parsing → split(), splitlines()
# ✔ Formatting → join(), format(), f-string
# ✔ Validation → isdigit(), isalpha(), isalnum()
# ✔ Search → find(), count(), startswith(), endswith()

# ===============================================================================
# File handling (read, write, with open) / file i/o in python

# f = open("data.json","a+") 
# f.write('\n{Hello, World! , i am arman and i lerning python , using ai}')
# data = f.read()
# print(data)
# f.close()

# with open("exam.txt","r") as f:
#     data = f.read()
#     if (data.find("java" ) != -1):
#         print("yes is present")
#     else:
#         print("not present")

# ==================================================================================

# OOP in Python (class, object, inheritance, polymorphism)


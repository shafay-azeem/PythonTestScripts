
import copy
import json
# Question 01:

# List Example
# name_list = ["Shafay", "Faizan", "Yawar"]
# name_list.append("Maisum")
# print(name_list)


# Tuple example
# point = (3, 5)
# x, y = point
# print(f"The coordinates are x={x} and y={y}")


# Question 02:

# def fibonacci(n):
#     a, b = 0, 1
#     for i in range(n):
#         yield a
#         a, b = b, a + b

# for i in fibonacci(10):
#     print(i)


# Question 03:

# def count_character_occurrences(input_string):
#     char_occurrences = {}
#     for char in input_string:
#         if char in char_occurrences:
#             char_occurrences[char] += 1
#         else:
#             char_occurrences[char] = 1
#     return char_occurrences


# input_string = "hello"
# occurrences = count_character_occurrences(input_string)
# print(occurrences)


# Question 04:

# def divide_numbers(a, b):
#     try:
#         result = a / b
#         print("The result of the division is:", result)
#     except ZeroDivisionError:
#         print("Error: Cannot divide by zero.")

# # divide_numbers(10, 2)
# # divide_numbers(5, 0)


# Question 05

# Shallow Copy
# original_list = [1, 2, [3, 4]]
# copied_list = copy.copy(original_list)

# copied_list[2][0] = 5

# print(original_list)
# print(copied_list)

# Deep Copy
# original_list = [1, 2, [3, 4]]
# copied_list = copy.deepcopy(original_list)

# copied_list[2][0] = 5

# print(original_list)
# print(copied_list)


# Question 07:

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def calculate_area(self):
#         return self.width * self.height

#     def calculate_perimeter(self):
#         return 2 * (self.width + self.height)


# rectangle = Rectangle(4, 5)
# area = rectangle.calculate_area()
# perimeter = rectangle.calculate_perimeter()

# print(f"The area of the rectangle is: {area}")
# print(f"The perimeter of the rectangle is: {perimeter}")


# Question 08:
# import json

# with open('myData.json', 'r') as file:
#     json_data = file.read()

# python_obj = json.loads(json_data)
# print(python_obj)


# Question 09:
# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):

#         print("Executing the decorator before the original function")

#         result = original_function(*args, **kwargs)

#         print("Executing the decorator after the original function")

#         return result

#     return wrapper_function


# @decorator_function
# def greet(name):
#     print(f"Hello, {name}!")


# greet("Shafay")


# Question 10:

# def get_even_numbers(numbers):
#     even_numbers = []
#     for num in numbers:
#         if num % 2 == 0:
#             even_numbers.append(num)
#     return even_numbers


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_numbers = get_even_numbers(numbers)
# print(even_numbers)

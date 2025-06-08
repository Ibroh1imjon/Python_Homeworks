#1
python -m venv myenv
myenv\Scripts\activate
pip install requests pandas


#2
#math_operations.py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

#string_utils.py
def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)


#3
#geometry/circle.py
import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius

#file_operations/file_reader.py
def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

#file_operations/file_writer.py
def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

#4
from math_operations import add, divide
from string_utils import reverse_string, count_vowels

from geometry.circle import calculate_area, calculate_circumference
from file_operations.file_reader import read_file
from file_operations.file_writer import write_file

print(add(5, 3))
print(divide(10, 2))
print(reverse_string("Hello"))
print(count_vowels("Hello World"))

print(calculate_area(5))
print(calculate_circumference(5))

write_file("sample.txt", "This is a test.")
print(read_file("sample.txt"))

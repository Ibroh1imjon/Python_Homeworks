# Exeption handling
# 1
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

# 2
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Error: Invalid integer input.")

# 3
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found.")

# 4
try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    result = float(num1) + float(num2)
except TypeError:
    print("Error: Inputs must be numerical.")
except ValueError:
    print("Error: Invalid number input.")

# 5
try:
    with open("protected_file.txt", "r") as file:
        content = file.read()
except PermissionError:
    print("Error: Permission denied.")

# 6
my_list = [1, 2, 3]
try:
    print(my_list[5])
except IndexError:
    print("Error: Index out of range.")

# 7
try:
    num = int(input("Enter a number: "))
except KeyboardInterrupt:
    print("\nInput was interrupted by the user.")

# 8
try:
    result = 10 / 0
except ArithmeticError:
    print("Error: Arithmetic error occurred.")

# 9
try:
    with open("file_with_encoding_issue.txt", "r", encoding="utf-8") as file:
        content = file.read()
except UnicodeDecodeError:
    print("Error: Encoding issue encountered.")

# 10
my_dict = {"key": "value"}
try:
    print(my_dict.upper())  # No 'upper' method for a dictionary
except AttributeError:
    print("Error: Attribute not found.")


#Files
# 1
try:
    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Error: File not found.")

# 2
try:
    n = int(input("Enter the number of lines to read: "))
    with open('example.txt', 'r') as file:
        for i in range(n):
            print(file.readline(), end='')
except FileNotFoundError:
    print("Error: File not found.")

# 3
try:
    with open('example.txt', 'a') as file:
        text = "This is a new line of text."
        file.write(text + '\n')
        print("Text has been appended.")
except FileNotFoundError:
    print("Error: File not found.")

# 4
try:
    n = int(input("Enter the number of lines to read from the end: "))
    with open('example.txt', 'r') as file:
        lines = file.readlines()
        print(''.join(lines[-n:]))
except FileNotFoundError:
    print("Error: File not found.")

# 5
try:
    lines = []
    with open('example.txt', 'r') as file:
        for line in file:
            lines.append(line.strip())
    print(lines)
except FileNotFoundError:
    print("Error: File not found.")

# 6
try:
    content = ''
    with open('example.txt', 'r') as file:
        for line in file:
            content += line
    print(content)
except FileNotFoundError:
    print("Error: File not found.")

# 7
try:
    content = []
    with open('example.txt', 'r') as file:
        content = file.readlines()
    print(content)
except FileNotFoundError:
    print("Error: File not found.")

# 8
try:
    with open('example.txt', 'r') as file:
        words = file.read().split()
        longest_word = max(words, key=len)
        print("Longest word:", longest_word)
except FileNotFoundError:
    print("Error: File not found.")

# 9
try:
    with open('example.txt', 'r') as file:
        lines = file.readlines()
        print("Number of lines:", len(lines))
except FileNotFoundError:
    print("Error: File not found.")

# 10
from collections import Counter
try:
    with open('example.txt', 'r') as file:
        words = file.read().split()
        word_count = Counter(words)
        print(word_count)
except FileNotFoundError:
    print("Error: File not found.")

# 11
import os
try:
    file_size = os.path.getsize('example.txt')
    print("File size:", file_size, "bytes")
except FileNotFoundError:
    print("Error: File not found.")

# 12
my_list = ['apple', 'banana', 'cherry']
try:
    with open('example.txt', 'w') as file:
        file.write('\n'.join(my_list))
    print("List has been written to the file.")
except FileNotFoundError:
    print("Error: File not found.")

# 13
try:
    with open('example.txt', 'r') as file:
        content = file.read()
        with open('copy_example.txt', 'w') as new_file:
            new_file.write(content)
    print("File content has been copied.")
except FileNotFoundError:
    print("Error: File not found.")

# 14
try:
    with open('file1.txt', 'r') as file1, open('file2.txt', 'r') as file2:
        lines1 = file1.readlines()
        lines2 = file2.readlines()
        combined_lines = [line1.strip() + ' ' + line2.strip() for line1, line2 in zip(lines1, lines2)]
    print(''.join(combined_lines))
except FileNotFoundError:
    print("Error: File not found.")

# 15
import random
try:
    with open('example.txt', 'r') as file:
        lines = file.readlines()
        random_line = random.choice(lines)
        print("Random line:", random_line)
except FileNotFoundError:
    print("Error: File not found.")

# 16
try:
    with open('example.txt', 'r') as file:
        if file.closed:
            print("File is closed.")
        else:
            print("File is still open.")
except FileNotFoundError:
    print("Error: File not found.")

# 17
try:
    with open('example.txt', 'r') as file:
        content = file.read().replace('\n', '')
        print("File content without newlines:", content)
except FileNotFoundError:
    print("Error: File not found.")

# 18
try:
    with open('example.txt', 'r') as file:
        text = file.read()
        word_count = len(text.split())
        print("Number of words:", word_count)
except FileNotFoundError:
    print("Error: File not found.")

# 19
try:
    with open('example.txt', 'r') as file:
        characters = list(file.read())
    print("Characters in the file:", characters)
except FileNotFoundError:
    print("Error: File not found.")

# 20
import string
try:
    for letter in string.ascii_uppercase:
        with open(f'{letter}.txt', 'w') as file:
            file.write(letter)
    print("26 text files created.")
except FileNotFoundError:
    print("Error: File not found.")

# 21
try:
    with open('alphabet.txt', 'w') as file:
        for i in range(0, 26, 5):
            file.write(''.join(chr(65 + j) for j in range(i, min(i + 5, 26))) + '\n')
    print("Alphabet written to file.")
except FileNotFoundError:
    print("Error: File not found.")


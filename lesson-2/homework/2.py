#1
name = input("Ismingiz: ")
birth_year = int(input("Tug‘ilgan yilingiz: "))
age = 2025 - birth_year
print("Yosh:", age)

#2
txt = 'LMaasleitbtui'
car1 = txt[1::2]
car2 = txt[0::2]
print("Car names:", car1, "va", car2)

#3
txt = 'MsaatmiazD'
car1 = txt[::2]
car2 = txt[::-2]
print("Car names:", car1, "va", car2)

#4
txt = "I'am John. I am from London"
start = txt.find("from ") + 5
area = txt[start:]
print("Joy:", area)

#5
s = input("Matn kiriting: ")
print("Teskarisi:", s[::-1])

#6
s = input("Matn kiriting: ")
vowels = "aeiouAEIOU"
count = 0
for c in s:
    if c in vowels:
        count = count + 1
print("Unli harflar soni:", count)

#7
numbers = [2, 45, 12, 39, 1]
max_num = numbers[0]
for n in numbers:
    if n > max_num:
        max_num = n
print("Eng katta son:", max_num)

#8
word = input("So‘z kiriting: ")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Palindrome emas")

#9
email = input("Email: ")
domain = email.split("@")[1]
print("Domen:", domain)

#10
import random
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
password = ''
for i in range(12):
    password = password + random.choice(chars)
print("Parol:", password)


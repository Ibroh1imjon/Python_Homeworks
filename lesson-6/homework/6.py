#1
def insert_underscores(txt):
    vowels = 'aeiou'
    result = ''
    c = ''
    i = 0
    count = 0
    while i < len(txt):
        result += txt[i]
        count += 1
        if count == 3:
            if txt[i] not in vowels and (i+1 >= len(txt) or txt[i+1] != '_') and txt[i] not in c:
                result += '_'
                c += txt[i]
                count = 0
            else:
                count -= 1
        i += 1
    if result.endswith('_'):
        result = result[:-1]
    return result
print(insert_underscores("hello"))          
print(insert_underscores("assalom"))       
print(insert_underscores("abcabcabcdeabcdefabcdefg"))

#2
n = int(input())
for i in range(n):
    print(i**2)

# 3.1
i = 1
while i <= 10:
    print(i)
    i += 1

# 3.2
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=' ')
    print()

# 3.3
n = int(input())
total = 0
for i in range(1, n + 1):
    total += i
print("Sum is:", total)

# 3.4
num = int(input())
for i in range(1, 11):
    print(num * i)

# 3.5
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if 100 < num < 200:
        print(num)

# 3.6
n = int(input())
count = 0
while n != 0:
    n //= 10
    count += 1
print("Output:", count)

# 3.7
for i in range(5, 0, -1):
    for j in range(i, 0, -1):
        print(j, end=' ')
    print()

# 3.8
list1 = [10, 20, 30, 40, 50]
for item in reversed(list1):
    print(item)

# 3.9
for i in range(-10, 0):
    print(i)

# 3.10
for i in range(5):
    print(i)
else:
    print("Done!")

# 3.11
start = 25
end = 50
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)

# 3.12
a, b = 0, 1
for _ in range(10):
    print(a, end=' ')
    a, b = b, a + b
print()

# 3.13
n = int(input())
fact = 1
for i in range(2, n + 1):
    fact *= i
print(f"{n}! = {fact}")

#4
list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
result = []
for item in list1:
    if item not in list2:
        result.append(item)
for item in list2:
    if item not in list1:
        result.append(item)
print(result)




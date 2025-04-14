# 1. Create and Access List Elements
fruits = ["olma", "banan", "gilos", "anor", "shaftoli"]
print("1. Uchinchi meva:", fruits[2])

# 2. Concatenate Two Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("2. Yangi list:", combined)

# 3. Extract Elements from a List
numbers = [10, 20, 30, 40, 50]
first = numbers[0]
middle = numbers[len(numbers)//2]
last = numbers[-1]
extracted = [first, middle, last]
print("3. Ajratilgan elementlar:", extracted)

# 4. Convert List to Tuple
movies = ["Inception", "Interstellar", "Matrix", "Avatar", "Tenet"]
movies_tuple = tuple(movies)
print("4. Tuplega aylantirilgan:", movies_tuple)

# 5. Check Element in a List
cities = ["London", "New York", "Tokyo", "Paris", "Berlin"]
is_paris = "Paris" in cities
print("5. Paris ro'yxatda bormi?", is_paris)

# 6. Duplicate a List Without Using Loops
numbers = [1, 2, 3]
duplicated = numbers * 2
print("6. Ikki baravar:", duplicated)

# 7. Swap First and Last Elements of a List
nums = [10, 20, 30, 40, 50]
nums[0], nums[-1] = nums[-1], nums[0]
print("7. O'zgarishdan so'ng:", nums)

# 8. Slice a Tuple
nums_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
slice_result = nums_tuple[3:8]
print("8. Kesilgan qism:", slice_result)

# 9. Count Occurrences in a List
colors = ["blue", "red", "blue", "green", "blue", "yellow"]
blue_count = colors.count("blue")
print("9. Nechta 'blue' bor:", blue_count)

# 10. Find the Index of an Element in a Tuple
animals = ("cat", "dog", "lion", "tiger", "elephant")
lion_index = animals.index("lion")
print("10. Lion indexi:", lion_index)

# 11. Merge Two Tuples
t1 = (1, 2, 3)
t2 = (4, 5, 6)
merged = t1 + t2
print("11. Birlashtirilgan tuple:", merged)

# 12. Find the Length of a List and Tuple
my_list = [1, 2, 3, 4, 5]
my_tuple = (10, 20, 30)
print("12. List uzunligi:", len(my_list))
print("12. Tuple uzunligi:", len(my_tuple))

# 13. Convert Tuple to List
nums_tuple = (1, 2, 3, 4, 5)
nums_list = list(nums_tuple)
print("13. Tuple dan list:", nums_list)

# 14. Find Maximum and Minimum in a Tuple
num_tuple = (7, 2, 9, 1, 5)
print("14. Eng katta:", max(num_tuple))
print("14. Eng kichik:", min(num_tuple))

# 15. Reverse a Tuple
words = ("hello", "world", "python", "tuple")
reversed_tuple = words[::-1]
print("15. Teskarisi:", reversed_tuple)

import numpy as np

# 1. Convert List to 1D Array
lst = [12.23, 13.32, 100, 36.32]
arr = np.array(lst)
print("Original List:", lst)
print("One-dimensional NumPy array:", arr)

# 2. Create 3x3 Matrix (2 to 10)
matrix = np.arange(2, 11).reshape(3, 3)
print("3x3 Matrix:")
print(matrix)

# 3. Null Vector (10) & Update Sixth Value
null_vector = np.zeros(10)
null_vector[5] = 11
print("Null Vector (10):")
print(np.zeros(10))
print("Update sixth value to 11:")
print(null_vector)

# 4. Array from 12 to 38
arr = np.arange(12, 39)
print("Array from 12 to 38:")
print(arr)

# 5. Convert Array to Float Type
arr = np.array([1, 2, 3, 4])
float_arr = arr.astype(float)
print("Original array:", arr)
print("Array converted to float type:", float_arr)

# 6. Celsius to Fahrenheit Conversion
celsius = np.array([0, 12, 45.21, 34, 99.91])
fahrenheit = (celsius * 9/5) + 32
print("Values in Celsius:", celsius)
print("Values in Fahrenheit:", fahrenheit)

# 7. Append Values to Array
arr = np.array([10, 20, 30])
arr = np.append(arr, [40, 50, 60, 70, 80, 90])
print("Original array:", [10, 20, 30])
print("After append values to the end of the array:", arr)

# 8. Array Statistical Functions
arr = np.random.random(10)
mean = np.mean(arr)
median = np.median(arr)
std_dev = np.std(arr)
print("Array:", arr)
print("Mean:", mean)
print("Median:", median)
print("Standard Deviation:", std_dev)

# 9. Find Min and Max in 10x10 Array
arr = np.random.random((10, 10))
min_val = np.min(arr)
max_val = np.max(arr)
print("10x10 Random Array:")
print(arr)
print("Minimum Value:", min_val)
print("Maximum Value:", max_val)

# 10. Create a 3x3x3 Array with Random Values
arr = np.random.random((3, 3, 3))
print("3x3x3 Random Array:")
print(arr)

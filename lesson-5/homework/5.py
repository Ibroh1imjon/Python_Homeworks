#1
year = int(input("Yilni kiriting: "))
if year % 400 == 0:
    print(f"{year} kabisa yili.")
elif year % 100 == 0:
    print(f"{year} kabisa yili emas.")
elif year % 4 == 0:
    print(f"{year} kabisa yili.")
else:
    print(f"{year} kabisa yili emas.")

#2
n = int(input("Enter a positive integer (1-100): "))
if n % 2 != 0:
    print("Weird")
elif 2 <= n <= 5:
    print("Not Weird")
elif 6 <= n <= 20:
    print("Weird")
else:
    print("Not Weird")

#3.1
a = 4
b = 15
start = a if a % 2 == 0 else a + 1
end = b if b % 2 == 0 else b - 1
if start <= end:
    even_numbers = list(range(start, end + 1, 2))
else:
    even_numbers = []
print(even_numbers)

#3.2
a = 4
b = 15
start = a + (a % 2)
end = b - (b % 2)
even_numbers = list(range(start, end + 1, 2))
print(even_numbers)


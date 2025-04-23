# 1. is_prime(n) funksiyasi
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 2. digit_sum(k) funksiyasi
def digit_sum(k):
    return sum(int(digit) for digit in str(k))

# 3. Ikki sonning darajalari (2 ning darajalari)
def power_of_two(N):
    powers = []
    i = 1
    while i <= N:
        powers.append(i)
        i *= 2
    return powers

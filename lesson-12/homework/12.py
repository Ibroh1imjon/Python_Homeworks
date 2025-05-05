###1
import threading
import math

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Function to check primes in a given range
def check_primes(start, end, primes_list):
    for num in range(start, end):
        if is_prime(num):
            primes_list.append(num)

# Function to divide the range and spawn threads
def threaded_prime_checker(start, end, num_threads):
    threads = []
    primes_list = []
    range_size = (end - start) // num_threads

    # Create and start threads
    for i in range(num_threads):
        thread_start = start + i * range_size
        thread_end = start + (i + 1) * range_size if i < num_threads - 1 else end
        thread = threading.Thread(target=check_primes, args=(thread_start, thread_end, primes_list))
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    return primes_list

# Example usage
start = 1
end = 100
num_threads = 4

primes = threaded_prime_checker(start, end, num_threads)
print(f"Prime numbers between {start} and {end}: {sorted(primes)}")



###2
import threading
from collections import defaultdict

# Function to process a chunk of the file and count words
def count_words_in_chunk(start, end, file, word_count):
    file.seek(start)
    chunk = file.read(end - start)
    words = chunk.split()
    
    # Count words in the current chunk
    local_count = defaultdict(int)
    for word in words:
        local_count[word.lower()] += 1

    # Add to the shared word count dictionary
    with threading.Lock():
        for word, count in local_count.items():
            word_count[word] += count

# Function to divide the file and spawn threads
def threaded_file_word_count(filename, num_threads):
    word_count = defaultdict(int)

    with open(filename, 'r') as file:
        file.seek(0, 2)  # Go to the end of the file
        file_size = file.tell()
        chunk_size = file_size // num_threads
        threads = []

        for i in range(num_threads):
            start = i * chunk_size
            end = (i + 1) * chunk_size if i < num_threads - 1 else file_size
            thread = threading.Thread(target=count_words_in_chunk, args=(start, end, file, word_count))
            threads.append(thread)
            thread.start()

        # Wait for all threads to finish
        for thread in threads:
            thread.join()

    return word_count

# Example usage
filename = "large_text_file.txt"
num_threads = 4

word_count = threaded_file_word_count(filename, num_threads)
print("Word counts:", dict(word_count))

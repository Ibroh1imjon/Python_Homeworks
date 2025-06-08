import json
import requests
import random
import os

# ---------- Task 1: JSON Parsing ----------
def parse_students_json(file_path='students.json'):
    if not os.path.exists(file_path):
        print("students.json not found.")
        return
    with open(file_path, 'r') as file:
        students = json.load(file)
        for student in students:
            print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")

# ---------- Task 2: Weather API ----------
def fetch_weather(city="Tashkent"):
    api_key = "your_openweather_api_key"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Description: {data['weather'][0]['description']}")
    else:
        print("Failed to fetch weather data.")

# ---------- Task 3: JSON Modification ----------
def modify_books_json(file_path='books.json'):
    if not os.path.exists(file_path):
        with open(file_path, 'w') as file:
            json.dump([], file)

    with open(file_path, 'r') as file:
        books = json.load(file)

    while True:
        print("\nBook Manager: 1-Add, 2-Update, 3-Delete, 4-Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Title: ")
            author = input("Author: ")
            books.append({"title": title, "author": author})
        elif choice == '2':
            title = input("Enter title to update: ")
            for book in books:
                if book["title"] == title:
                    book["title"] = input("New Title: ")
                    book["author"] = input("New Author: ")
                    break
        elif choice == '3':
            title = input("Enter title to delete: ")
            books = [book for book in books if book["title"] != title]
        elif choice == '4':
            break

    with open(file_path, 'w') as file:
        json.dump(books, file, indent=4)
    print("Changes saved.")

# ---------- Task 4: Movie Recommendation ----------
def recommend_movie_by_genre(genre):
    api_key = "your_omdb_api_key"
    search_url = f"http://www.omdbapi.com/?apikey={api_key}&s={genre}&type=movie"
    response = requests.get(search_url)
    if response.status_code == 200:
        results = response.json()
        if 'Search' in results:
            movie = random.choice(results['Search'])
            movie_id = movie['imdbID']
            detail_url = f"http://www.omdbapi.com/?apikey={api_key}&i={movie_id}"
            detail_resp = requests.get(detail_url)
            if detail_resp.status_code == 200:
                info = detail_resp.json()
                print(f"\nTitle: {info['Title']}")
                print(f"Year: {info['Year']}")
                print(f"Genre: {info['Genre']}")
                print(f"Plot: {info['Plot']}")
            else:
                print("Error fetching movie details.")
        else:
            print("No movies found.")
    else:
        print("Failed to access OMDB API.")

# ---------- Main ----------
def main():
    while True:
        print("\nMenu:")
        print("1. Parse Students JSON")
        print("2. Fetch Weather for Tashkent")
        print("3. Modify Books JSON")
        print("4. Recommend Movie by Genre")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            parse_students_json()
        elif choice == '2':
            fetch_weather()
        elif choice == '3':
            modify_books_json()
        elif choice == '4':
            genre = input("Enter movie genre: ")
            recommend_movie_by_genre(genre)
        elif choice == '5':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

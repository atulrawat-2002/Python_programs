import os
import json

FILENAME = "movies.json"

def load_movies():
    if not os.path.exists(FILENAME):
        return []
    else:
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)

def save_movies(movies):
    if not os.path.exists(FILENAME):
        return
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(movies, f, indent=2)

def add_movies(movies):
    title = input("Enter the title: ").strip().lower()
    if any( movie["Title"].lower() == title for movie in movies ):
        print("Movie already exists")
        return
    genre = input("Enter genre: ").strip().lower()
    rating = float(input("Enter rating (0-10): "))
    try: 
        if not (0 <= rating <=10):
            raise ValueError
    except ValueError:
        print("Please enter a valid number ")
    movies.append({"Title": title, "Genre": genre, "Rating": rating})
    save_movies(movies)
    print("Movie added ✅")
    return

def search_movies(movies):
    term = input("Enter the search term: ").strip().lower()
    for movie in movies:
        result = [movie for movie in movies if term in movie["Title"] or term in movie["Genre"]]
    if not result:
        print("No matching result!")
        return
    else:
        print(f"Found {len(result)} results ")
        for movie in result:
            print(f" {movie["Title"]} -- {movie["Genre"]} -- {movie["Rating"]} ")


def view_movies(movies):
    if not movies:
        print("No moveis found ")
        return
    print("-"*30)
    for movie in movies:
            print(f" {movie["Title"]} -- {movie["Genre"]} -- {movie["Rating"]} ")
    print("-"*30)


def run_movies_DB():
    movies = load_movies()

    while True:
        print("\n MoviesDB")
        print("1. Add Movie")
        print("2. Search Movie")
        print("3. View all movies")
        print("4. Exit")

        choice = input('Enter your choice: ').strip()

        match choice:
            case "1": add_movies(movies)
            case "2": search_movies(movies)
            case "3": view_movies(movies)
            case "4": break
            case _: print("Enter a valid choice ")


if __name__ == "__main__":
    run_movies_DB()
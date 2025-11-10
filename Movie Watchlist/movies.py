import json
import os

MOVIES_FILE = "movies.json"

def load_movies():
    """Load movies from JSON file"""
    if os.path.exists(MOVIES_FILE):
        try:
            with open(MOVIES_FILE, 'r') as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    return []

def save_movies(movies):
    """Save movies to JSON file"""
    with open(MOVIES_FILE, 'w') as file:
        json.dump(movies, file, indent=2)

def add_movie(movies):
    print("\n Adding a movie...")
    
    title = input("Enter movie title: ").strip()
    if not title:
        print("Title cannot be empty!")
        return movies
    
    year = input("Enter movie year: ").strip()
    if not year.isdigit():
        print("Year must be a number!")
        return movies
    
    movie = {
        "title": title,
        "year": int(year),
        "watched": False
    }
    
    movies.append(movie)
    save_movies(movies)
    print(f"✅ '{title}' ({year}) added successfully!")
    return movies

def list_movies(movies):
    """List all movies with their status"""
    print("\n--- All Movies ---")
    
    if not movies:
        print("No movies in your list yet.")
        return
    
    for index, movie in enumerate(movies, 1):
        status = "✅ watched" if movie["watched"] else "❌ not watched"
        print(f"{index}. {movie['title']} ({movie['year']}) - {status}")

def mark_as_watched(movies):
    """Mark a movie as watched by index"""
    print("\n--- Mark as Watched ---")
    
    if not movies:
        print("No movies in your list yet.")
        return movies
    
    list_movies(movies)
    
    try:
        index = int(input("\nEnter the number of the movie to mark as watched: "))
        if 1 <= index <= len(movies):
            movies[index-1]["watched"] = True
            save_movies(movies)
            print(f"✅ '{movies[index-1]['title']}' marked as watched!")
        else:
            print("Invalid movie number!")
    except ValueError:
        print("Please enter a valid number!")
    
    return movies

def display_menu():
    """Display the main menu"""
    print("🎬 MOVIE TRACKER")
    print("="*40)
    print("1. Add a movie")
    print("2. List all movies")
    print("3. Mark as watched")
    print("4. Quit")
    print("="*40)


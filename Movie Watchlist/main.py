from movies import save_movies, load_movies, display_menu, add_movie, list_movies, mark_as_watched
def main():
    """Main program loop"""
    movies = load_movies()
    
    print("🎬 Welcome to Movie Tracker!")
    
    while True:
        display_menu()
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            movies = add_movie(movies)
        elif choice == "2":
            list_movies(movies)
        elif choice == "3":
            movies = mark_as_watched(movies)
        elif choice == "4":
            print("\n🎉 Thanks for using Movie Tracker! Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please enter 1-4.")

if __name__ == "__main__":
    main()
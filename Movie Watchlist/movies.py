import json 

title = input("Enter movie name: ")
year = input("Enter year of movie")

movie = [] #load exisiting movies or create empty list 


new_movie = {
    "name": title, 
    "year": year, 
    "watched": False
}
movie.append(new_movie)

with open('movietest.json', 'w', encoding='utf-8') as file:
    json.dump(movie, file, indent=4, ensure_ascii=False)

#confirm the above stores input into json file 

#now to print all movies / LIST MOVIES 

with open('movietest.json', 'r', encoding='utf-8') as file: 
    loaded_data =json.load(file)

print(loaded_data)
#Get name of movie, enter name, if name matches table change to true 
query = input("Search a movie: ").strip().lower()

found = False 
for movie in loaded_data: 
    if movie['name'].lower() == query: 
        movie['watched'] = True #change status to true 
        print(f"Marked {movie['name']} as watched")
        found = True 
        break 

if not found: 
    print("Movie not found")

#saved the updaed data 
with open('movietest.json', 'w', encoding='utf-8') as file: 
    json.dump(loaded_data, file, indent=4, ensure_ascii=False)

#print updated 
for movie in loaded_data: 
    print(f"Name: {movie['name']}, Year: {movie['year']}, Watched: {movie['watched']}")
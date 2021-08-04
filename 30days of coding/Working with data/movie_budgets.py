# a program to check out the budgets of movies

movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]



# allow users to add n number of movies to the list
number = int(input("Enter the number of movies you will like to add: \n>"))

for i in range(number):
    movie = input("Enter the name of the movie: \n>")
    budget = input("Enter the budget of the movie: \n>")

    new_movie = (movie, int(budget))
    movies.append(new_movie)



# calculate the average budget of all movies
total = 0
for movie in movies:
    total += movie[1]

avg = total/len(movies)

# print movies that have budgets above average budget and how much higher they have
# also print the length of movies above average
moviess = []
for movie in movies:
    movie_name = movie[0]
    movie_budget = movie[1]

    if movie_budget > avg:
        print(f"{movie_name}, has a budget higher than the average budget with {movie_budget - avg}")
        moviess.append(movie)

print(f"There are {len(moviess)} that spent above the average budget")
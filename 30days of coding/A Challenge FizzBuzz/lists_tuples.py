# a program to createand manipulate lists and tuples

# create a list containing a single tuple
# the tuple should follow the following format (movie_title, director_name, release_year, budget)
movies = [("Jumanji", "D'Rock", "2020", "$100,000")]

# prompt user to enter information for a new tuple with same information as the first
movie_title = input("Enter the title of the movie: ").strip()
director_name = input("Enter the name of the director: ").strip()
release_year = input("Enter the year the movie was released: ").strip()
budget = input("Enter the total budget of the movie: ").strip()

# create  a new tuple from the inputed response
new_tuple = (movie_title, director_name, release_year, budget)
print(movie_title, release_year)

# add the new tuple to the list
movies.append(new_tuple)
print(movies)

del movies[0]
print(movies)
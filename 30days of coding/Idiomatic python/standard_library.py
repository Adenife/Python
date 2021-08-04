from collections import namedtuple, defaultdict


Movie = namedtuple("Movie", ("title", "director", "year"))

title = input("Enter movie title: ").strip().title()
director = input("Enter movie director: ").strip().title()
year = input("Enter movie year of release: ").strip().title()

movie = Movie(title = title, director = director, year = year)
print(f"{movie.title} ({movie.year}) - {movie.director}")



# Use a defaultdict to store a count for each character that appears in a given string. 
# Print the most common character in this dictionary.

string_count = defaultdict(int)

def add_item(item):
    for items in item: 
        string_count[items] += 1

add_item("onomatopoeia")
most_common_character = max(string_count, key=lambda key: string_count[key])
print(string_count)
print(most_common_character)


# Use the mul function in the operator module to create a partial called double 
# that always provides 2 as the first argument.
from operator import mul
from functools import partial

double = partial(mul, 2)

# Create a read function using a partial that opens a file in read ("r") mode.
read = partial(open, mode='r')
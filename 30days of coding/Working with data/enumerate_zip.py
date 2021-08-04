# examples using the enumerate and zip functions

main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]

for name, actor, animal in main_characters:
    print(f"{name}, is a {animal.lower()} voiced by {actor}")


# unpacking values to different variables
new = ("John Smith", 11743, ("Computer Science", "Mathematics"))
name, id_number, (major, minor) = new




# using zip function
names = ["John", "Anne", "Peter"]
ages = [26, 31, 29]

for name, age in zip(names, ages):
	print(f"{name} is {age} years old.")

# zipping containers of different length
from itertools import zip_longest

l_1 = [1, 2, 3]
l_2 = [1, 2]

combinated = list(zip_longest(l_1, l_2, fillvalue="_"))

print(combinated)

# zipping in reverse
zipped = [("John", 26), ("Anne", 31), ("Peter", 29)]
names, ages = zip(*zipped)

print(names)  
print(ages)




# using the enumerate function
movies = [
	(
		"Eternal Sunshine of the Spotless Mind",
		"Michel Gondry",
		2004
	),
	(
		"Memento",
		"Christopher Nolan",
		2000
	),
	(
		"Requiem for a Dream",
		"Darren Aronofsky",
		2000
	)
]

for counter, (title, director, year) in enumerate(movies, start=1):
	print(f"{counter}. {title} ({year}), by {director}")
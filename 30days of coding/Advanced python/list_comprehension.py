# comprehensions in python are used to write smart codes
numbers = [1, 2, 3, 4, 5]

# normal loop
# squares = []

# for number in numbers:
# 	squares.append(number ** 2)

# list comprehension
numbers = [number**2 for number in numbers]
print(numbers)


# using comprehensions with dictionaries
movie = {
	"title": "thor: ragnarok",
	"director": "taika waititi",
	"producer": "kevin feige",
	"production_company": "marvel studios"
}

movie = {
    key: value.title()
    for key, value in movie.items()
}
print(movie)
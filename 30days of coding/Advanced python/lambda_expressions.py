# how to work with functions and lambda expressions

# sort the dictionary in alphabetical order
students = [
	{"name": "Hannah", "grade_average": 83},
	{"name": "Charlie", "grade_average": 91},
	{"name": "Peter", "grade_average": 85},
	{"name": "Rachel", "grade_average": 79},
	{"name": "Lauren", "grade_average": 92}
]

sorted_students = sorted(students, key=lambda student: student["name"])
print(sorted_students)


# define an exponential function using lambda
expo = lambda number, exponent: number ** exponent

print(expo(3,2))
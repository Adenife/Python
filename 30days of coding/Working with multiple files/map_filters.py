# how to use the map and filter functions in python

# using maps in python
humpty_dumpty = [
	"  Humpty Dumpty sat on a wall,  ",
	"Humpty Dumpty had a great fall;     ",
	"  All the king's horses and all the king's men ",  
	"    Couldn't put Humpty together again."
]

rhymes = list(map(lambda rhym: rhym.strip(), humpty_dumpty))
print(*rhymes, sep = "\n")
# print(rhymes)


# using conditional comprehensions
names = ("bob", "Christopher", "Rachel", "MICHAEL", "jessika", "francine")
name = [name for name in names if len(name) < 8]
print(name)


# using filters
def remove_neg(num):
    return num > 0

numbers = list(range(-5, 11))
number = list(filter(remove_neg, numbers))
print(*number)
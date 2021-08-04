#  how to accept multiple values in a function

# a function to sum up n number of items (positional)
def sum(*numbers):
    total = 0
    for number in numbers:
        total += number

    print(total)


# a function to accept n number of positional and keyword arguments
def show_it(*args, **kwargs):
    for item in args:
        print(f"{item} is a positional argument")

    for item in kwargs:
        print(f"{item} is a keyword argument")




# print the dictionary using the .format and destructuring
country = {
	"name": "Germany",
	"population": "83 million",
	"capital": "Berlin",
	"currency": "Euro"
}

country_template = """Name: {name}
Population: {population}
Capital: {capital}
Currency: {currency}"""

print(country_template.format(**country))
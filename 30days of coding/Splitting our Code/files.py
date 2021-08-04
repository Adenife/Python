# program to show how to work with files in pyhton

irises = [
	{'sepal_length': '5.1', 'sepal_width': '3.5', 'petal_length': '1.4', 'petal_width': '0.2', 'species': 'Iris-setosa'},
	{'sepal_length': '4.9', 'sepal_width': '3',   'petal_length': '1.4', 'petal_width': '0.2', 'species': 'Iris-setosa'},
	{'sepal_length': '4.7', 'sepal_width': '3.2', 'petal_length': '1.3', 'petal_width': '0.2', 'species': 'Iris-setosa'},
	{'sepal_length': '4.6', 'sepal_width': '3.1', 'petal_length': '1.5', 'petal_width': '0.2', 'species': 'Iris-setosa'},
	{'sepal_length': '5',   'sepal_width': '3.6', 'petal_length': '1.4', 'petal_width': '0.2', 'species': 'Iris-setosa'},
	{'sepal_length': '7',   'sepal_width': '3.2', 'petal_length': '4.7', 'petal_width': '1.4', 'species': 'Iris-versicolor'},
	{'sepal_length': '6.4', 'sepal_width': '3.2', 'petal_length': '4.5', 'petal_width': '1.5', 'species': 'Iris-versicolor'},
	{'sepal_length': '6.9', 'sepal_width': '3.1', 'petal_length': '4.9', 'petal_width': '1.5', 'species': 'Iris-versicolor'},
	{'sepal_length': '5.5', 'sepal_width': '2.3', 'petal_length': '4',   'petal_width': '1.3', 'species': 'Iris-versicolor'},
	{'sepal_length': '6.5', 'sepal_width': '2.8', 'petal_length': '4.6', 'petal_width': '1.5', 'species': 'Iris-versicolor'},
	{'sepal_length': '6.3', 'sepal_width': '3.3', 'petal_length': '6',   'petal_width': '2.5', 'species': 'Iris-virginica'},
	{'sepal_length': '5.8', 'sepal_width': '2.7', 'petal_length': '5.1', 'petal_width': '1.9', 'species': 'Iris-virginica'},
	{'sepal_length': '7.1', 'sepal_width': '3',   'petal_length': '5.9', 'petal_width': '2.1', 'species': 'Iris-virginica'},
	{'sepal_length': '6.3', 'sepal_width': '2.9', 'petal_length': '5.6', 'petal_width': '1.8', 'species': 'Iris-virginica'},
	{'sepal_length': '6.5', 'sepal_width': '3',   'petal_length': '5.8', 'petal_width': '2.2', 'species': 'Iris-virginica'}
]

# convert list of dictionaries to csv
with open("./Splitting our Code/iris.txt", 'a') as cursor:
    for items in irises:
        cursor.write(",".join(items.values()))
        cursor.write("\n")
    # cursor.write("\nYou are going to love uaing this")


# read in csv file and convert to dictionary
with open("./Splitting our Code/irisfile.csv", "r") as iris_file:
	iris_data = iris_file.readlines()

headers = iris_data[0].strip().split(",")
irises = []

for row in iris_data[1:]:
	iris = row.strip().split(",")
	iris_dict = dict(zip(headers, iris))

	irises.append(iris_dict)

print(irises)
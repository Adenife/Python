# program to perform set operations in python

# create an empty set
my_set = set()

# add 3 values to the set
my_set.add("Mimi")
my_set.update(["Bolu", "Nife"])

# create a second set
second_set = {"Adeola", "Mimi", "Seyitan"}

# find the union of the set
print(my_set.union(second_set))

# find the symmetric difference of the set (order doesnt matter)
print(second_set.symmetric_difference(my_set))

# find the intersection of the set
print(my_set.intersection(second_set))

# find the difference of the set (order matters)
print(my_set.difference(second_set))


# testing the in keyword in python
num = int(input("Enter a number: \n>"))

num_list = range(18, 25)
# num_list = []
# for i in range(18,25):
#     num_list.append(i)

if num in num_list:
    print("The number entered is in range!")
elif num < num_list[0]:
    print("Number lower than range!!!")
else:
    print("Number higher than range!!!")
print("##############################")
print("  WELCOME TO THE DBS CONSOLE  ")
print("##############################")


number_of_elements = int(input("Input the number of elements to be stored in the list: "))


elements = []
for i in range(number_of_elements):
    input_value = input(f"element - {i}: ")
    elements.append(input_value)


unique_list = list(set(elements))


for items in unique_list:
    print(f"{items} occurs {elements.count(items)} times")
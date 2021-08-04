# guessing game
# exact = 53
# number = int(input("Enter a number to get started: \n>"))

# while True:
#     if number > exact:
#         print("Too large")
#     elif number < exact:
#         print("Too small")
#     else:
#         print("Exact")
#         break

#     number = int(input("Enter a number to get started: \n>"))
new = []
for i in range (2, 10):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        new.append(str(i))

print(", ".join(new))


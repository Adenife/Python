# the following list of tuples contain information about employee name, hours worked weekly and hourly rate
employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]

# total = []
# for workers in employees:
#     hrly_rate = workers[2]
#     total.append(hrly_rate)

# avg = sum(total)/len(total)

total = 0
for worker in employees:
    total += worker[2]

avg = total/len(employees)


for employee in employees:
    name = employee[0]
    hrs_worked = employee[1]
    hrly_rate = employee[2]

    wage = hrs_worked * hrly_rate
    # print(f"{name}, is to be paid ${wage} this week")
    if hrly_rate > avg:
        print(f"{name}, earns above average hourly rate")
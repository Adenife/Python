# a simple program to calculate the total earings of an employee per week

# take in the name, hourly wage and number of hours worked per week
name = input("Enter your full name: \n")
hrly_wage = input("Enter your hourly wage rate: \n")
hrs_worked = input("Enter the number of hours worked this week: \n")

# format user input. 
# strip name of white spaces and make it title space
name = name.strip().title()

# convert hrly wage and hrs worked to numerical values
hrly_wage = float(hrly_wage)
hrs_worked = float(hrs_worked)

# calculate the total earnings per week
total_earnings = hrly_wage * hrs_worked

# print the result
print(f"{name} earned {total_earnings} this week")
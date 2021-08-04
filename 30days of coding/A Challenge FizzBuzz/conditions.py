# prompt user to enter a number and display if the number is positive, negative or neutral
usr_input = int(input("Enter an integer: \n"))

# check if the number is positive, negative or neutral
if usr_input == 0:
    print(f"{usr_input}, is Zero")
elif usr_input > 0:
    print(f"{usr_input}, is positive")
else:
    print(f"{usr_input}, is negative")


# program to determine if an employee is owed overtime
# prompt user to input info
name = input("Please enter your name: \n").strip()
hrly_wage = input("Enter your hourly wage: \n")
hrs_worked = input("Enter the number of hours worked: \n")

if float(hrs_worked) > 40:
    extr_hrs = float(hrs_worked) - 40
    percent_hrly_pay = float(hrly_wage) * 0.1
    total_add_pay = percent_hrly_pay * extr_hrs

    print(f"{name} should be paid additional ${total_add_pay:.3f} for working {extr_hrs} extra hours this week")
else:
    print("You have been fully paid!")
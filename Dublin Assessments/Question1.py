# Declare the normal working hours per week
NORMAL_HOURS = 37.50

# take in user input
name = input("Employee Name: ")
number = input("Employee Number: ")
week_ending = input("Week ending: ")
hour_worked = input("Number of hours worked: ")
hourly_rate = input("Hourly Rate: ")
overtime_rate = input("Overtime Rate: ")
tax_rate = input("Standard Tax Rate: ")
otax_rate = input("Overtime Tax Rate: ")


# Make calculations
total_normal_pay = NORMAL_HOURS * float(hourly_rate)
overtime_hours = float(hour_worked) - NORMAL_HOURS
total_overtime_pay = overtime_hours * float(overtime_rate)
tax_twenty = (float(tax_rate)/100) * total_normal_pay
tax_fifty = (float(otax_rate)/100) * total_overtime_pay
total_pay = total_normal_pay + total_overtime_pay
total_deduction = tax_fifty + tax_twenty
net_pay = total_pay - total_deduction


# Print result
print("\n                                Pay Slip ")
print(f"WEEK ENDING {week_ending}")
print(f"Employee: {name}")
print(f"Employee Number: {number}")
print("                      Earnings                                 Deductions")
print("                      Hours             Rate             Total   ")
print(f"Hours (normal)        {NORMAL_HOURS}              {hourly_rate}             {total_normal_pay} Tax @20% {tax_twenty}")
print(f"Hours (overtime)      {overtime_hours}               {overtime_rate}            {total_overtime_pay}  Tax @50% {tax_fifty}\n")
print(f"                                   Total Pay:                   {total_pay}")
print(f"                                   Total Deductions:            {total_deduction}")
print(f"                                   Net Pay:                     {net_pay}")
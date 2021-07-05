import os
import csv

# Variables
total_number_of_months = 0
net_total_amount = 0
monthly_change = []
month_count = []
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greatest_decrease_month = 0

# Set Path For File
csvpath = os.path.join(".", "PyBank", "Resources", "budget_data.csv")

# Open
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
     # Read The Header
    csv_header = next(csvreader)
    row = next(csvreader)
    
    # Calculate
    previous_row = int(row[1])
    total_number_of_months += 1
    net_total_amount += int(row[1])
    greatest_increase = int(row[1])
    greatest_increase_month = row[0]
    
    # Read Each Row
    for row in csvreader:
        total_number_of_months += 1
        net_total_amount += int(row[1])

        # Current Month To Previous Month
        revenue_change = int(row[1]) - previous_row
        monthly_change.append(revenue_change)
        previous_row = int(row[1])
        month_count.append(row[0])
        
        # Calculate The Greatest Increase
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        # Calculate The Greatest Decrease
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]  
        
    # Calculate The Average & The Date
    average_change = sum(monthly_change)/ len(monthly_change)
    
    highest = max(monthly_change)
    lowest = min(monthly_change)

# Print Analysis
print(f"Financial Analysis")
print(f"---------------------------")
print(f"Total Months: {total_number_of_months}")
print(f"Total: ${net_total_amount}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})")

# save the output file path
output_file = os.path.join(".", "PyBank", "analysis", "budget_data_revised.text")

with open(output_file, 'w',) as txtfile:
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Months: {total_number_of_months}\n")
    txtfile.write(f"Total: ${net_total_amount}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {greatest_increase_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {greatest_decrease_month}, (${lowest})\n")
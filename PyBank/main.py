import os
import csv

# path to file
csvpath = os.path.join("..", "PyBank", "Resources", "budget_data.csv")

# Store data
total = []
months = []
month_change = []
greatest_increase_month = 0
greatest_decrease_month = 0
greatest_increase = 0
greatest_decrease = 0

# calculation 
def average (numbers):
    total = 0
    for number in numbers:
        total += number
    find_average = total/len(numbers)
    return find_average

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # remove header
    csv_header = next(csvfile)
    # append rows
    for row in csvreader:
        months.append(row[0])
        total.append(row[1])
        month_change.append(int(row[1]))
        
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]
            
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]
 

    # find net amount profit and losses
    total_revenue = 0
    for values in total:
        total_revenue += int(values)
    print(f'Financial Analysis')
    print(f'-----------------------------')
    print(f'Total Months: {len(months)}')
    print(f'Total: ${total_revenue}')
    net_revenue = [j-i for i,j in zip(month_change[:-1], month_change[1:])]
    print(f'Average Change: ${round(average(net_revenue),2)}')
    net_revenue.sort(reverse=True)
    print(f'Greatest Increase in Profits: {greatest_increase_month}, ${net_revenue[0]}')
    print(f'Greatest Decrease in Profits: {greatest_decrease_month}, ${net_revenue[len(net_revenue)-1]}')
    
# output to analysis
output_path = os.path.join("..", "PyBank", "analysis", "Analysis.txt")
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['------------------------------'])
    csvwriter.writerow([f'Total Months: {len(months)}'])
    csvwriter.writerow([f'Total: ${total_revenue}'])
    csvwriter.writerow([f'Average Change: ${round(average(net_revenue),2)}'])
    csvwriter.writerow([f'Greatest Increase in Profits: {greatest_increase_month} (${net_revenue[0]})'])
    csvwriter.writerow([f'Greatest Decrease in Profits: {greatest_decrease_month} (${net_revenue[len(net_revenue)-1]})'])
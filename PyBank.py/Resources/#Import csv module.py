#Import csv module
import csv

#Create lists to store values for analysis
dates = []
values = []
changes = []

#Read csv file, store headings separately, and populate dates and values lists with data
with open (C:/Users/Jojof/Download/starter_code.py/starter_code/PyBank.py/Resources/Budget_data.csv)
    csv_reader = csv.reader("csvfile")
    headings = next("csvreader")
    for row in csv_reader:
        dates.append(row[0])
        values.append(int(row[1]))

#Calculate number of months
total_months = len(dates)

#Calculate net total of profits and losses
net_total = sum(values)

#Calculate and store changes in values month to month, then calculate average change
previous_value = values[0]
for value in values[1::]:
    change = value - previous_value
    changes.append(change)
    previous_value = value
average_change = round((sum(changes) / len(changes)), 2)

#Calculate max increase and decrease, and find corresponding months
max_increase = max(changes)
max_increase_month = dates[(changes.index(max_increase)) + 1]
max_decrease = min(changes)
max_decrease_month = dates[(changes.index(max_decrease)) + 1]

#Print results to terminal
print("Financial Analysis\n")
print("----------------------\n")
print("Total Months: " + str(total_months) + "\n")
print("Total: $" + str(net_total) + "\n")
print("Average Change: $" + str(average_change) + "\n")
print("Greatest Increase in Profits: " + max_increase_month + " ($" + str(max_increase) + ")\n")
print("Greatest Decrease in Profits: " + max_decrease_month + " ($" + str(max_decrease) + ")")

#Create output .txt file and write results into file
output_file = open("C:/Users/adina/Desktop/Classwork/Module 3 Python/Module 3 Challenge/python-challenge/PyBank/Analysis/PyBank_Analysis.txt", "w")

output_file.write("Financial Analysis\n")
output_file.write("----------------------\n")
output_file.write("Total Months: " + str(total_months) + "\n")
output_file.write("Total: $" + str(net_total) + "\n")
output_file.write("Average Change: $" + str(average_change) + "\n")
output_file.write("Greatest Increase in Profits: " + max_increase_month + " ($" + str(max_increase) + ")\n")
output_file.write("Greatest Decrease in Profits: " + max_decrease_month + " ($" + str(max_decrease) + ")")

output_file.close()
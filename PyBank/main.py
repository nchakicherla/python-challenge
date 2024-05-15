import os
import csv

csv_input_path = os.path.join('.', 'Resources', 'budget_data.csv')

with open(csv_input_path) as f:

	reader = csv.reader(f, delimiter=',')
	header = next(reader)

	number_months_measured = 0
	net_amount = 0


	month_change = []
	month_change_name = []
	prev_month = 0

	for row in reader:
		number_months_measured += 1
		net_amount += int(row[1])
		if(number_months_measured != 1):
			month_change.append( int(row[1]) - int(prev_month))
			month_change_name.append(row[0])
		prev_month = int(row[1])

	f.close()


max_index = month_change.index(max(month_change))
max_monthly_increase = month_change[max_index]
max_month = month_change_name[max_index]

min_index = month_change.index(min(month_change))
min_monthly_increase = month_change[min_index]
min_month = month_change_name[min_index]


# write to terminal
print("Financial Analysis")
print("----------------------------")
print("Total Months:", number_months_measured)
print("Total: $" + str(net_amount))
print("Average Change: $" + str(round(sum(month_change) / len(month_change), 2)))
print("Greatest Increase in Profits: " + str(max_month) + " ($" + str(max_monthly_increase) + ")")
print("Greatest Decrease in Profits: " + str(min_month) + " ($" + str(min_monthly_increase) + ")")

# write output file
output_write_path = os.path.join(".", "analysis", "analysis.txt")

with open(output_write_path, "w") as f:
	f.write("Financial Analysis\n")
	f.write("----------------------------\n")
	f.write("Total Months: " + str(number_months_measured) + "\n")
	f.write("Total: $" + str(net_amount) + "\n")
	f.write("Average Change: $" + str(round(sum(month_change) / len(month_change), 2)) + "\n")
	f.write("Greatest Increase in Profits: " + str(max_month) + " ($" + str(max_monthly_increase) + ")\n")
	f.write("Greatest Decrease in Profits: " + str(min_month) + " ($" + str(min_monthly_increase) + ")")
	f.close()
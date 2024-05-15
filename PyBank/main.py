import os
import csv

csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

	csvreader = csv.reader(csvfile, delimiter=',')
	next(csvreader)

	number_months_measured = 0
	net_amount = 0


	month_change = []
	month_change_name = []
	prev_month = 0

	for row in csvreader:
		number_months_measured += 1
		net_amount += int(row[1])
		if(number_months_measured != 1):
			month_change.append( int(row[1]) - int(prev_month))
			month_change_name.append(row[0])
		prev_month = int(row[1])

'''
print(number_months_measured)
print(net_amount)
print(sum(month_change) / len(month_change))
#print(month_change.index(max(month_change)))

max_index = month_change.index(max(month_change))
min_index = month_change.index(min(month_change))

print(month_change_name[max_index], month_change[max_index])
print(month_change_name[min_index], month_change[min_index])
'''
max_index = month_change.index(max(month_change))
max_monthly_increase = month_change[max_index]
max_month = month_change_name[max_index]

min_index = month_change.index(min(month_change))
min_monthly_increase = month_change[min_index]
min_month = month_change_name[min_index]

print("Financial Analysis")
print("----------------------------")
print("Total Months:", number_months_measured)
print("Total: $" + str(net_amount))
print("Average Change: $" + str(round(sum(month_change) / len(month_change), 2)))
print("Greatest Increase in Profits: " + str(max_month) + " ($" + str(max_monthly_increase) + ")")

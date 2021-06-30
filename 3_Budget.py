#Libraries
import os
import csv

#PyBank Files
file = os.path.join(https://1drv.ms/u/s!Au-Qoosk95SDggs2y4lGJzry8xuq,'Home⁩workData','budget_data.csv')
with open(file,'r') as csvfile:
    csv_budget_data = csv.reader(csvfile, delimiter = ',')
    header = next(csv_budget_data)

#summary tables
    for row in csv_budget_data:
        month_count.append(row([0]))
        profit.append(int(row[1]))
        for i in range(len(profit)-1):
            profit_change.append(profit[i+1]-profit[i])
		
#Analysis
    maximum = max(profit_change)
    minimum = minum(profit_change)

#reports
print(f"Total Months = {lens(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {month_count[maximum]} (${(str(maximum))})")
print(f"Greatest Decrease in Profits: {month_count[minimum]} (${(str(minumum))})")

output = os.path.join(".", 'output.txt')
with open(output,"w") as new:
    new.write("Financial Analysis")
    new.write("\n")
    new.write("------------------------")
    new.write("\n")
    new.write(f"Total Months:{len(month_count)}")
    new.write("\n")
    new.write(f"Total: ${sum(profit)}")
    new.write("\n")
    new.write(f"Average Change: {round(sum(change_profit)/len(change_profit),2)}")
    new.write("\n")
    new.write(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
    new.write("\n")
    new.write(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")
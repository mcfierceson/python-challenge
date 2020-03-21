# Polling python script

import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    months = []
    lastMonth = "None"
    lastTotal = 0
    grandTotal = 0
    change = []

    # Read each row of data after the header
    for row in csvreader:

        thisMonth = row[0]
        thisTotal = int(row[1])

        months.append(thisMonth)
        change.append(thisTotal - lastTotal)

        grandTotal = grandTotal + thisTotal
        lastTotal = int(row[1])
        

    avgChange = sum(change) / len(change)
    maxMonth = change.index(max(change))
    minMonth = change.index(min(change))

    print("\nFinancial Analysis")
    print("---------------------------")
    print(f"Total Months: {len(months)}")
    print(f"Total: ${grandTotal}")
    print(f"Average Change: ${round(avgChange,2)}")
    print(f"Greatest Increase in Profits: {months[maxMonth]} (${max(change)})")
    print(f"Greatest Decrease in Profits: {months[minMonth]} (${min(change)})\n")
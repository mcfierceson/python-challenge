# Polling python script

import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    names = []
    votes = []

    # Read each row of data after the header
    for row in csvreader:

        lastName = row[2]
        rowVotes = int(row[0])

        if lastName not in names:
            names.append(lastName)
            votes.append(rowVotes)
        else:
            nameIndex = names.index(lastName)
            currTotal = votes[nameIndex] + rowVotes
            votes[nameIndex] = currTotal
        
    totalVotes = sum(votes)

    print("\nElection Results")
    print("---------------------------------")
    print(f"Total Votes: {totalVotes}")
    print("---------------------------------")

    for x in range(len(names)):
        percentage = round((votes[x] / totalVotes) * 100, 3)
        print(f"{names[x]}: {percentage}%  ({votes[x]})")
    print("---------------------------------")
    
    winner = names[votes.index(max(votes))]

    print(f"Winner: {winner}")
    print("---------------------------------\n")

import os

import csv

num_rows = 0

candidates = set()

csvpath = os.path.join( 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)
    csv_header = next(csvreader)

      

    for row in csvreader:

        num_rows +=1
    
        
        
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    for row in csvreader:
        candidates.add(row[2])
    print(candidates) 
    
    for current in csvreader:
        
        if current == previous:
            PnLchange = 0
        elif previous == "382539":
            break
        else:
            PnLchange = int(current) - int(previous)
        PnL_change_list.append(PnLchange)
        previous = current
    
        
    
    
print("Election Results")
print("                                ")
print("----------------------------")
print("                               ")
print(f"Total Votes: {num_rows}")
print("----------------------------")


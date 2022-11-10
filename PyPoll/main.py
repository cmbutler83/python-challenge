import os

import csv

num_rows = 0
csvpath = os.path.join( 'Resources', 'election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)

    for row in csvreader:

        num_rows +=1
    
    
    
    
    
    
    
    
    
    print("Election Results")
    print("                                ")
    print("----------------------------")
    print("                               ")
    print(f"Total Votes: {num_rows}")


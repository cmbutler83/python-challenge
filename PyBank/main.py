# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv



csvpath = os.path.join( 'Resources', 'budget_data.csv')

# # Method 1: Plain Reading of CSV files
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))


# Method 2: Improved Reading using CSV module

with open(csvpath) as csvfile:
 
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    
    # Read each row of data after the header and count number of months
    num_rows = 0
    PnL_net = 0
    PnL_change = 0
    for row in csvreader:
        num_rows +=1
        if row[1] == 0:
            PnL_net = 0
        else:
            PnL_net = int(PnL_net) + int(row[1])

        if row[1] ==0:
            PnL_change = 0
        else:
            PnL_change = int(row[1])-int(PnL_change)

    print (f"Total Months:  {str(num_rows)}" )
    print (f"Total: $ {str(PnL_net)}")
    print (f"{str(PnL_change)}")
        
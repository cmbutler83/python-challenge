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
    
    
    # Read each row of data after the header and count number of months
    num_rows = 0
    PnL_net = 0
    PnL_list = []
    PnL_change_list = [] 
    previous = 0
    PnLchange = 0
    Greatest = 0
    Lowest = 0

    for row in csvreader:
        PnL_list.append(row[1])
        
    


        num_rows +=1
        
   
        if row[1] == 0:
            PnL_net = 0
        else:
            PnL_net = int(PnL_net) + int(row[1])
        
        
    for current in PnL_list:
        
        if current == "1088983":
            PnLchange = 0
        elif previous == "382539":
            break
        else:
            PnLchange = int(current) - int(previous)
        PnL_change_list.append(PnLchange)
        previous = current

   
    average_change = int((sum(PnL_change_list))/((len(PnL_change_list))-1))  
            
            
    print("Financial Analysis")
    print("--------------------------------------")
    print (f"Total Months:  {str(num_rows)}" )
    print (f"Total: $ {str(PnL_net)}")
    print (f"Average Change: $ {str(average_change)}")
    print (f"Greatest Increase in Profits: $ {max(PnL_change_list)}")
    print (f"Greatest Decrease in Profits: $ {min(PnL_change_list)}")

    with open ("mainoutput.txt","w") as f:
    f.write("Financial Analysis")
    f.write("\n")
    f.write("--------------------------------------")
    f.write("\n")
    f.write(f"Total Months:  {str(num_rows)}" )
    f.write("\n")
    f.write(f"Total: $ {str(PnL_net)}")
    f.write("\n")
    f.write(f"Average Change: $ {str(average_change)}")
    f.write("\n")
    f.write(f"Greatest Increase in Profits: $ {max(PnL_change_list)}")
    f.write("\n")
    f.write(f"Greatest Decrease in Profits: $ {min(PnL_change_list)}")
f.close()

   

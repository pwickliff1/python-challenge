import os
import csv

csvpath = os.path.join( 'Resources', 'budget_data.csv')
txtpath  = open("PyBankReport.txt", "w")


# Initialize variables
row_cnt = 0
profit = 0
old_row = 0
change = 0
change_save = 0
greatest_profit = 0
least_profit = 0

with open(csvpath) as csvfile:
 
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)
    
    # Read each row of data after the header
    for row in csvreader:
        
        # Keep track on # of rows
        row_cnt += 1
        
        # Add each months profit
        profit =  profit + int(row[1])
                
        # Save the row with the greatest profit
        if greatest_profit < (int(row[1]) - old_row):
            greatest_profit = (int(row[1]) - old_row)
            greatest_date = row[0]
            
        # Save the row with the least profit
        if least_profit > (int(row[1]) - old_row):
            least_profit =(int(row[1]) - old_row)
            least_date = row[0]
                
        # Add each month loss/profit unless except for first row
        if old_row != 0:
            change = change + (int(row[1]) - old_row)
                 
        old_row = int(row[1])

# Print report to screen
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(row_cnt))
print("Total: $" + str(profit))
print("Average Change: $" + str(round(change/(row_cnt-1),2)))
print("Greatest Increase in Profits: " + greatest_date[3:] + "-20" + greatest_date[0:2] + " ($" + str(greatest_profit) + ")" )
print("Greatest Decrease in Profits: " + least_date[3:] + "-20" + least_date[0:2] + " ($" + str(least_profit) + ")" )


txtpath.write("Financial Analysis\n" )
txtpath.write("----------------------------\n")
txtpath.write("Total Months: " + str(row_cnt) + "\n")
txtpath.write("Total: $" + str(profit) + "\n")
txtpath.write("Average Change: $" + str(round(change/(row_cnt-1),2)) + "\n")
txtpath.write("Greatest Increase in Profits: " + greatest_date[3:] + "-20" + greatest_date[0:2] + " ($" + str(greatest_profit) + ")\n" )
txtpath.write("Greatest Decrease in Profits: " + least_date[3:] + "-20" + least_date[0:2] + " ($" + str(least_profit) + ")" )
txtpath.close()

import os
import csv
import pandas as pd

# Open files
csvpath = os.path.join('Resources', 'election_data.csv')
txtpath  = open("PyRollReport.txt", "w")

# Initialize variables
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
Otooley_votes = 0
row_cnt = 0

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
  
    # Read each row of data after the header
    for row in csvreader:
        
        # Keep count of row (total votes cast)
        row_cnt += 1
        
        # Count Khan votes
        if row[2] == "Khan":
            Khan_votes += 1
         
        # Count Correy votes
        if row[2] == "Correy":
           Correy_votes += 1
                
        # Count Li votes
        if row[2] == "Li":
            Li_votes += 1
        
        # Count O'Tooley votes
        if row[2] == "O'Tooley":
            Otooley_votes += 1

# Create and sort dataframe using election results
election_results = {'Votes': [Khan_votes,Correy_votes,Li_votes,Otooley_votes],'Name': ['Khan','Correy','Li','O\'Tooley']}
pd_results = pd.DataFrame(election_results)
pd_sorted_results = pd_results.sort_values("Votes", ascending=False)                     
  
# Print report to screen
print("Election Results")
print("-------------------------")
print("Total Votes:  " + str(row_cnt) )        
print("-------------------------")   
for x in range(0, 4):
    print(pd_sorted_results.iloc[x]['Name'] + ": " + "{:.3f}".format((pd_sorted_results.iloc[x]['Votes']/row_cnt)*100) + "% (" + str(pd_sorted_results.iloc[x]['Votes']) + ")") 
print("-------------------------")   

# Print report to file
txtpath.write("Election Results\n")
txtpath.write("-------------------------\n")
txtpath.write("Total Votes:  " + str(row_cnt) + "\n" )        
txtpath.write("-------------------------\n")   
for x in range(0, 4):
    txtpath.write(pd_sorted_results.iloc[x]['Name'] + ": " + "{:.3f}".format((pd_sorted_results.iloc[x]['Votes']/row_cnt)*100) + "% (" + str(pd_sorted_results.iloc[x]['Votes']) + ")\n") 
txtpath.write("-------------------------")   

# Close output file
txtpath.close()

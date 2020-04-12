# Import dependencies
import os, csv
from pathlib import Path 

# Assign file location with the pathlib library
csv_file_path = Path("election_data.csv")

# Declare my variables 
total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Open csv in default read mode with context manager
with open(csv_file_path,newline="", encoding="utf-8") as elections:

    # Store data under the csvreader variable
    csvreader = csv.reader(elections,delimiter=",") 

    # Skip the header so we iterate through the actual values
    header = next(csvreader)     

    # Iterate through each row in the csv
    for row in csvreader: 

        # Count the unique Voter ID's and store in a variable called total_votes
        total_votes +=1

        # If the name of the candidate is found, count the times it appears and store in a list
        # We can use this values in our percent vote calculation in the print statements at the end
        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

 # To find the winner we make a dictionary of the two lists we created before
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [khan_votes, correy_votes, li_votes, otooley_votes]

# We zip together the list of candidate(as key) and the total votes(as value)
# Get winner with a max of the dictionary 
dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)

# For print on the terminal the summary of the analysis
khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

# Print the summary table using the f sugar 
print(f"Election Results")
print(f"----------------------------")
print(f"Total Votes: {total_votes}")
print(f"----------------------------")
print(f"Khan: {khan_percent:.3f}% ({khan_votes})")
print(f"Correy: {correy_percent:.3f}% ({correy_votes})")
print(f"Li: {li_percent:.3f}% ({li_votes})")
print(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
print(f"----------------------------")
print(f"Winner: {key}")
print(f"----------------------------")

# Print results to an outside text file with "w"

with open("poll_analysis.txt","w") as txtfile:

# Write methods to print to Elections_Results_Summary 
    txtfile.write(f"Election Results")
    txtfile.write("\n")
    txtfile.write(f"----------------------------")
    txtfile.write("\n")
    txtfile.write(f"Total Votes: {total_votes}")
    txtfile.write("\n")
    txtfile.write(f"----------------------------")
    txtfile.write("\n")
    txtfile.write(f"Khan: {khan_percent:.3f}% ({khan_votes})")
    txtfile.write("\n")
    txtfile.write(f"Correy: {correy_percent:.3f}% ({correy_votes})")
    txtfile.write("\n")
    txtfile.write(f"Li: {li_percent:.3f}% ({li_votes})")
    txtfile.write("\n")
    txtfile.write(f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})")
    txtfile.write("\n")
    txtfile.write(f"----------------------------")
    txtfile.write("\n")
    txtfile.write(f"Winner: {key}")
    txtfile.write("\n")
    txtfile.write(f"----------------------------")
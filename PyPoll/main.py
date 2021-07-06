import os
import csv

# path to file 
csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

# store data
candidate_list = []
total_votes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
Otooley_votes = 0

# open/read file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    for row in csvreader:
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            
        # total votes    
        total_votes += 1    
        
        if row[2] == candidate_list[0]:
            Khan_votes += 1
        elif row[2] == candidate_list[1]:
            Correy_votes += 1
        elif row[2] == candidate_list[2]:
            Li_votes += 1
        elif row[2] == candidate_list[3]:
            Otooley_votes += 1 

# calculate percent
Khan_percent = Khan_votes / total_votes * 100
Correy_percent = Correy_votes / total_votes * 100
Li_percent = Li_votes / total_votes * 100
Otooley_percent = Otooley_votes / total_votes * 100

# winner
winner = max(Khan_votes, Correy_votes, Li_votes, Otooley_votes)
if winner == Khan_votes:
    winner_name = "Khan"
elif winner == Correy_votes:
    winner_name = "Correy"
elif winner ==  Li_votes:
    winner_name = "Li"  
else :
    winner_name = "O'tooley"     

# print 
print(f"Election Results")
print(f"------------------------")
print(f"Total Votes: {total_votes}")
print(f"------------------------")
print(f"Khan: {Khan_percent:.3}% ({Khan_votes})")
print(f"Correy: {Correy_percent:.3}% ({Correy_votes})")
print(f"Li: {Li_percent:.3}% ({Li_votes})")
print(f"O'Tooley: {Otooley_percent:.3}% ({Otooley_votes})")
print(f"------------------------")
print(f"Winner: {winner_name}")
print(f"------------------------")

# output to analysis
output_path = os.path.join("..", "PyPoll", "analysis", "Election Results.txt")
with open(output_path, 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=',')
    csvwriter.writerow([f"Election Results"])
    csvwriter.writerow([f"------------------------"])
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow([f"------------------------"])
    csvwriter.writerow([f"Khan: {Khan_percent:.3}% ({Khan_votes})"])
    csvwriter.writerow([f"Correy: {Correy_percent:.3}% ({Correy_votes})"])
    csvwriter.writerow([f"Li: {Li_percent:.3}% ({Li_votes})"])
    csvwriter.writerow([f"O'Tooley: {Otooley_percent:.3}% ({Otooley_votes})"])
    csvwriter.writerow([f"------------------------"])
    csvwriter.writerow([f"Winner: {winner_name}"])
    csvwriter.writerow([f"------------------------"])
 
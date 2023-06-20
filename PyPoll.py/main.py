import os
import csv

election_data=os.path.join("Resources","election_data.csv")

total_votes=0

winning_candidate=""
winning_count=0

candidate_options = [] #list
candidate_votes = {} #dictionary

with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes=total_votes+1

        cand_name=row[2]

        if cand_name not in candidate_options:
            candidate_options.append(cand_name)
            candidate_votes[cand_name] = 0

        candidate_votes[cand_name] += 1

    election_analysis=os.path.join("analysis", "election_analysis.txt")
with open(election_analysis, 'w') as txtfile:

     output = (f"Election Results\n"
                f"-------------------------\n"
                f"Total Votes: {total_votes}\n"
                f"-------------------------\n")

     txtfile.write(output)
     print(output) 

for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        percent = votes / total_votes * 100
        output = f"{candidate}: {percent:.3f}% ({votes})\n"
        txtfile.write(output)
        print(output)
        if votes > winning_count:
            winning_count = votes
            winning_candidate = candidate
        print("-------------------------")
        txtfile.write("-------------------------\n")

        winner=(f"Winner: {winning_candidate}\n")
        print(winner)
        txtfile.write(winner)

        print("-------------------------")
        txtfile.write("-------------------------\n")

        txtfile.close()    
# Add our dependencies
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join('Resources', 'election_results.csv')
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# 1. Initialize a total vote counter.
total_votes = 0

# Declare candidate list
candidate_options = []

# Declare candidate votes dictionary
candidate_votes = {}

# Winning Candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: perform analysis.
    
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row.
        candidate_name = row[2]
        # Add the candidate name to the candidate list.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        #Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Determine the percetage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and the percentage of votes.
    print(f"{candidate_name}: {vote_percentage: .1f}% ({votes:,})\n")

    # Determine willing vote count and candidate
    # Determine if the votes is greater than the winning count.
    if (votes>winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning count = votes and winning percent = vote percent.
        winning_count = votes
        winning_percentage = vote_percentage
        # And, set the winning candidate equal to the candidate's name.
        winning_candidate = candidate_name

# To do: print out the winning candidate, vote count, and percentage.
winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count: ,}\n"
    f"Winning Percentage: {winning_percentage: .1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
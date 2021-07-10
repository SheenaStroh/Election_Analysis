# Election_Analysis

## Project Overview
A Colorado Board of Electins employee has given you the following tasks to complete the election audit of recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3., Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.csv
- Software: Python 3.8.8, Visual Studio Code, 1.57.1

## Summary
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
  - Diana DeGette received 73.8% of the vote and 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
- The winner of the election was:
  - Diana DeGette, who recieved 73.8% of the vote and 272,892 votes.

## Challenge Overview
After completing the initial election audit, the election commission requested the following 
additional information:
- Voter turnout for each county
- The percentage of votes from each county out of the total count
- The county with the highest turnout.
Utilizing the same script that was used in the initial audit updates were added to gather the requested information.

## Challenge Results
The following information was gathered using the initial analysis code as a starting point:
- The total number of votes cast in the election was 369,711.
- The percentage and total votes in each county broke down as follows:
  - Jefferson:  10.5%   38,855
  - Denver:     82.8%   306,055
  - Arapahoe:   6.7%    24,801
- Denver county had the largest number of votes. This was determined using the following code, which 
  sets up a vote count for each county, and then compares each vote count to determine which is the 
  largest:
    
      for county_name in county_votes:
        county_count = county_votes.get(county_name)
        
        if (county_count > voter_turnout):
            voter_turnout = county_count
            largest_county = county_name
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
  - Diana DeGette received 73.8% of the vote and 272,892 votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes.
- The winner of the election was:
  - Diana DeGette, who recieved 73.8% of the vote and 272,892 votes.

## Challenge Summary
Overall, this script not only provides the requested information, but it can easily be used in other 
elections to get the same type of information. The code that was used to gather both the candidate 
and the county data was set up in such a way that it will capture all counties and candidates that 
have vote data provided.
        
    for row in reader:
        total_votes = total_votes + 1
        candidate_name = row[2]
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

        # If the county does not match any existing county in the county list, add it to the list.
        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1

In the above code all that might need to be changed is the index selection in the third and fourth 
row, to make sure the correct data was being collected from the main data file. Another example of 
some code that would need to be updated is the path and file name of the main data file noted in this 
code:
    
    file_to_load = os.path.join("..", "Resources", "election_results.csv")
    
With just these minor changes this script would be re-usable in basically any similar type of 
election.

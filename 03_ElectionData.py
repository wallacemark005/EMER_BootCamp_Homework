#Libraries
import os
import csv

#PyPoll Files
file = os.path.join('Home⁩workData','election_data.csv')
with open(file,'r') as csvfile:
        csv_budget_data = csv.reader(csvfile, delimiter = ',')
        header = next(csv_budget_data)

#Creates dictionary to be used for candidate name and vote count.
poll = {}

#Sets variable, total votes, to zero for count.
total_votes = 0

#gets data file
with open(file, 'r') as csvfile:
    csvread = csv.reader(csvfile)

#skips header line
    next(csvread, None)

#dictionary using 3 file columns as keys, using unique names
#vote total counts for each candidate by total vote count
    for row in csvread:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
 
#create empty list for candidates and his/her vote count
candidates = []
num_votes = []

#takes dictionary keys and values and, respectively, dumps them into the lists, 
#candidates and num_votes
for key, value in poll.items():
	candidates.append(key)
	num_votes.append(value)

# creates vote percent list
vote_percent = []
for n in num_votes:
	vote_percent.append(round(n/total_votes*100, 3))

# zips candidates, num_votes, vote_percent into tuples
clean_data = list(zip(candidates, num_votes, vote_percent))

#creates winner_list to put winners (even if there is a tie)
winner_list = []

for name in clean_data:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])

# makes winner_list a str with the first entry
winner = winner_list[0]

#only runs if there is a tie and puts additional winners into a string separated by commas
if len(winner_list) > 1:
	for w in range(1, len(winner_list)):
	    winner = winner + ", " + winner_list[w]
#prints to file
output_file = os.path.join('election_results.txt')

with open(output_file, 'w') as txtfile:
	txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) +  '\n-------------------------\n')
	for entry in clean_data:
		txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
	txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

#prints file to terminal
with open(output_file, 'r') as readfile:
	print(readfile.read())
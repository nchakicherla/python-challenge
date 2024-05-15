import os
import csv

# establish input .csv path
csv_input_path = os.path.join(".", "Resources", "election_data.csv")

with open(csv_input_path) as f:

	# create reader object
	reader = csv.reader(f, delimiter=",")
	# header saved as string
	header = next(reader)

	total_votes = 0
	unique_candidates = []
	tallies = dict()
	percentages = dict()

	# first pass through csv establishes unique 
	# candidates and tallies total votes
	for row in reader:
		total_votes += 1
		if (row[2] not in unique_candidates):
			unique_candidates.append(row[2])

	# populate tallies dictionary with initial zeroed counts
	# based on unique candidates established
	for cand in unique_candidates:
		tallies[cand] = 0

	# rewind file pointer and read through header again
	f.seek(0)
	next(reader)

	# second pass through csv tallies the number
	# of votes each unique candidate has, incrementing
	# the dictionary values
	for row in reader:
		tallies[row[2]] += 1

	f.close()

# percentages dictionary is populated by using values in tallies
# and dividing by total votes. x 100 for percent value
for cand in unique_candidates:
	percentages[cand] = tallies[cand] / total_votes * 100

# find the max value in percentages and retrieve 
# the key to store in winner
winner = max(percentages, key=percentages.get)

# print analysis to terminal
print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
for cand in unique_candidates:
	print(cand + ": " + str(round(percentages[cand], 3)) + "% (" + str(tallies[cand]) + ")")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

# establish output file path
output_write_path = os.path.join(".", "analysis", "analysis.txt")

# establish output file pointer and write analysis to file
with open(output_write_path, "w") as f:
	f.write("Election Results\n")
	f.write("-------------------------\n")
	f.write("Total Votes: " + str(total_votes) + "\n")
	f.write("-------------------------\n")
	for cand in unique_candidates:
		f.write(cand + ": " + str(round(percentages[cand], 3)) + "% (" + str(tallies[cand]) + ")\n")
	f.write("-------------------------\n")
	f.write("Winner: " + winner + "\n")
	f.write("-------------------------")
	
	f.close()

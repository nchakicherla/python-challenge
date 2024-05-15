import os
import csv

csv_input_path = os.path.join(".", "Resources", "election_data.csv")
#print(csv_input_path)

with open(csv_input_path) as f:

	reader = csv.reader(f, delimiter=",")
	header = next(reader)

	total_votes = 0
	unique_candidates = []

	for row in reader:
		total_votes += 1
		if (row[2] not in unique_candidates):
			unique_candidates.append(row[2])

	tallies = dict()
	for cand in unique_candidates:
		tallies[cand] = 0

	f.seek(0)
	next(reader) #skip header once more

	for row in reader:
		tallies[row[2]] += 1

	f.close()

percentages = dict()
for cand in unique_candidates:
	percentages[cand] = tallies[cand] / total_votes * 100

winner = max(percentages, key=percentages.get)

print("Election Results")
print("-------------------------")
print("Total Votes: " + str(total_votes))
print("-------------------------")
for cand in unique_candidates:
	print(cand + ": " + str(round(percentages[cand], 3)) + "% (" + str(tallies[cand]) + ")")
print("-------------------------")
print("Winner: " + winner)
print("-------------------------")

output_write_path = os.path.join(".", "analysis", "analysis.txt")

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

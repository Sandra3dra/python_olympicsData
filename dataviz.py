import csv
import matplotlib.pyplot as plt

golds = []
silvers = []
bronxes = []

categories = []

with open("data/OlympicsWinter.csv") as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			print("stripping out categories")
			categories.append(row)
			line_count +=1
		else:
			if row[7] == "Gold":
				print("Gold")
				golds.append(row[7])
			elif row[7] == "Silver":
				print("Silver")
				silver.append(row[7])
			elif row[7] == "Bronze":
				print("Bronze")
				bronze.append(row[7])
			line_count +=1


print(len(gold), "Gold medals were")
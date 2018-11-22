import csv

year_2014 = []

with open('data/OlympicsWinter.csv') as csvfile:
	reader = csv.reader(csvfile)
	line_count = 0

	for row in reader:
		if line_count is 0:
			print("stripping out categories")
			categories.append(row)
			line_count +=1

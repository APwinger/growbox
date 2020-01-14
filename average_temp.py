import csv

with open('humidity.csv') as csv_file:
	csv_reader = csv.reader(csv_file,  delimiter=',')
	line_count = 1
	l = []
	for row in csv_reader:
		temp = row[2]
		hum = row[3]
		l.append(temp)
		line_count += 1
		print(line_count)
	average = sum(l)/integer(line_count)
	print(l)


import csv
import datetime

with open('dReddit.csv', 'a') as csv_file:
	writer = csv.writer(csv_file)
	
	#The for loop
	for post_id, score in data:
		writer.writerow([post_id, score, datetime.now()])
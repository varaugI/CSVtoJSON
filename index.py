import csv
import json

with open('file.csv', 'r') as csvfile, open('file.json', 'w') as jsonfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        json.dump(row, jsonfile)
        jsonfile.write('\n')

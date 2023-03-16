import json
import csv

with open('clients.json', 'r') as f:
    file = json.load(f)

with open('clients.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=',')
    column = file[0].keys()
    writer.writerow(column)

    for i in file:
        writer.writerow(i.values())
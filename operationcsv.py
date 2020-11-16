import csv

file = open("data_file/record.csv", "r")

with file:
    read = csv.reader(file)
    for row in read:
        print(row)
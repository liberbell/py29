import csv

file = open("data_file/record.csv", "r")

with file:
    read = csv.reader(file)
    for row in read:
        print(row)

print("--------\n")

file = open("data_file/record_pipe.csv", "r")

with file:
    read = csv.reader(file)
    for row in read:
        print(row)

print("--------\n")

file = open("data_file/record_pipe.csv", "r")

with file:
    read = csv.reader(file, delimiter="|")
    for row in read:
        print(row)


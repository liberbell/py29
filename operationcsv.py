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

print("--------\n")

file = open("data_file/record_tab.csv", "r")

with file:
    read = csv.reader(file, delimiter="\t")
    for row in read:
        print(row)

print("--------\n")

file = open("data_file/record.csv", "r")

with file:
    read = csv.DictReader(file)
    for row in read:
        print(dict(row))

print("--------\n")

file = open("data_file/record.csv", "r")

with file:
    read = csv.DictReader(file)
    for row in read:
        print(row)

names = [["First Name", "Last Name"],
         ["Sofia", "Reyes"],
         ["Jerome", "Jackson"]
         ["Jia", "Zhong"]]

file = open("data_file/names.csv", "w")

with file:
    file_writer = csv.writer(file)
    for row in names:
        file_writer.writerow(row)
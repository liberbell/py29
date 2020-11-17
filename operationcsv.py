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
         ["Jerome", "Jackson"],
         ["Jia", "Zhong"]]

# file = open("data_file/names.csv", "w")

# with file:
#     file_writer = csv.writer(file)
#     for row in names:
#         file_writer.writerow(row)

nums = [[10, 20, 30],
        [40, 50, 60],
        [70, 80, 90]]

# file = open("data_file/numbers.csv", "w")

# with file:
#     write = csv.writer(file)
#     write.writerows(nums)

# file = open("data_file/names.csv", "w")

# with file:
#     fnames = ["First Name", "Last Name"]
#     writer = csv.DictWriter(file, fieldnames=fnames)

#     writer.writeheader()
#     writer.writerow(({"First Name" : "Sofia", "Last Name": "Reyes"}))
#     writer.writerow(({"First Name" : "Jerome", "Last Name": "Jackson"}))
#     writer.writerow(({"First Name" : "Jia", "Last Name": "Zhong"}))

# csv.register_dialect("tab", delimiter="\t")

# with open("data_file/record_tab.csv", "r") as f:
#     reader = csv.reader(f, dialect = "tab")

#     for row in reader:
#         print(row)

csv.register_dialect("plus", delimiter="+", lineterminator="\n\n\r")

file = open("data_file/names_dialect.csv", "w")

with file:
    file_writer = csv.writer(file, dialect="plus")
    for row in names:
        file_writer.writerow(row)
# open("data_file/example.txt")
# print(open("data_file/example.txt"))

# file = open("data_file/example.txt")
# print(file)

# print(file.mode)
# print(file.name)
# print(file.closed)

# file.close()
# print(file.closed)

# file = open("data_file/example.txt")
# print(file.read())

# print(file.seek(0))
# print(file.read(5))
# print(file.tell())
# print(file.read(5))

# print(file.tell())

# file.seek(0)
# print(file.tell())

# print(file.read(15))
# print(file.tell())
# print(file.read())

# file.close()

with open("data_file/example.txt") as f:
    data = f.readlines()

print(data)
print(f.closed)

with open("data_file/example.txt") as f:
    line = f.readline()

    while line:
        print(line)
        line = f.readline()

file = open("data_file/example.txt", "w")
file.close()
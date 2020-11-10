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

# with open("data_file/example.txt") as f:
#     data = f.readlines()

# print(data)
# print(f.closed)

# with open("data_file/example.txt") as f:
#     line = f.readline()

#     while line:
#         print(line)
#         line = f.readline()

# file = open("data_file/sample.txt", "w")
# file.close()

# file = open("data_file/sample.txt", "w")
# file.write("Let's check the write operation.")
# file.close()

# file = open("data_file/sample.txt")
# print(file.read())
# file.close()

# file = open("data_file/sample.txt", "w")
# file.write("Let's check the write operation.")

# file.seek(6)
# file.write(" examine ")
# file.close()

# file = open("data_file/sample.txt")
# print(file.read())
# file.close()

# file = open("data_file/sample.txt")
# for lines in file:
#     print(lines)
# file.close()

# with open("data_file/sample.txt", "w") as f:
#     f.write("First line\n")
#     f.write("Second line \n")
#     f.write("Third line\n")

# f = open("data_file/sample.txt", "a")
# print(f.tell())

# f.writelines(["Another line was appended\n",
#              "What will it look like now?\n",
#              "Let's check it out\n"])
# f.close()

# f = open("data_file/sample.txt", "r")
# print(f.readlines())
# print(f.fileno())
# print(f.isatty())
# print(f.readable())
# print(f.writable())
# f.close()

f = open("data_file/sample.txt", "a")
print(f.tell())
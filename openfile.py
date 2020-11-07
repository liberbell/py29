open("data_file/example.txt")
print(open("data_file/example.txt"))

file = open("data_file/example.txt")
print(file)

print(file.mode)
print(file.name)
print(file.closed)

file.close()
print(file.closed)

file = open("data_file/example.txt")
print(file.read())

print(file.seek(0))
print(file.read(5))
print(file.tell())
print(file.read(5))
file = open("sample.txt", "w")
file.write("Welcome to Python programming")
file.close()

file = open("sample.txt", "r")
content = file.read()
print(content)
file.close()
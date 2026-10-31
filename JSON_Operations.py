import json

student = {
    "name": "Aljo",
    "age": 23,
    "course": "MCA"
}

# Write JSON
with open("student.json", "w") as file:
    json.dump(student, file, indent=4)

# Read JSON
with open("student.json", "r") as file:
    data = json.load(file)

print(data)
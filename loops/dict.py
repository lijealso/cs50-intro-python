students = {
    "Hermione" : "Gryffindor",
    "Harry" : "Gryffindor", 
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin"
}
'''
print(students["Hermione"])
print(students["Draco"])
'''

for student in students:
    print(student, students[student], sep = ", ")
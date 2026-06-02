# Writing student names into file

file = open("students.txt", "w")

file.write("San\n")
file.write("Maggie\n")
file.write("Rahul\n")
file.write("Anu\n")
file.write("Suresh\n")

file.close()


# Reading file

file = open("students.txt", "r")

students = file.readlines()

print("Student Names:\n")

for name in students:
    print(name.strip())

file.close()


# Counting total students

print("\nTotal Students :", len(students))

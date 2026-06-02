students = {

    "San": {"Marks": 89, "Grade": "A"},
    "Maggie": {"Marks": 75, "Grade": "B"},
    "Rahul": {"Marks": 95, "Grade": "A+"},
    "Anu": {"Marks": 82, "Grade": "B+"},
    "Suresh": {"Marks": 91, "Grade": "A"}

}

print("Student Details\n")

for name, details in students.items():

    print("Name :", name)
    print("Marks :", details["Marks"])
    print("Grade :", details["Grade"])
    print()


# Finding highest marks
highest = 0
top_student = ""

for name, details in students.items():

    if details["Marks"] > highest:
        highest = details["Marks"]
        top_student = name


print("Student with Highest Marks")
print("Name :", top_student)
print("Marks :", highest)

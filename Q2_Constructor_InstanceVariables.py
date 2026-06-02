class Employee:

    def __init__(self, employee_id, employee_name, salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.salary = salary

    def display_details(self):
        print("Employee ID :", self.employee_id)
        print("Employee Name :", self.employee_name)
        print("Salary :", self.salary)
        print()


# Creating employee objects
emp1 = Employee(101, "rahul", 30000)
emp2 = Employee(102, "san", 40000)
emp3 = Employee(103, "maggie", 35000)

# Displaying details
emp1.display_details()
emp2.display_details()
emp3.display_details()

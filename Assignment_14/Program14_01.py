'''
    Create a class Employee with attributes name, emp_id, and salary. Create objects of this class and print their details using a method.
    
    Expected Output:
                    Name   : Rohit
                    ID     : 101
                    Salary : 50000
'''
# Class created
class Employee:
    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def display_details(self):
        print("Employee Name : ", self.name)
        print("Employee ID : ", self.emp_id)
        print("Employee Name : ", self.salary)

def main():
    # Create Employee object
    emp1 = Employee("Rohit", 101, 50000)

    # Instance Method Call
    emp1.display_details()

# starter
if __name__ == "__main__":
    main()                  # Function Call

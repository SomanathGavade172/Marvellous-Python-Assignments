'''
    4. Create a class Student with name, roll_no, and a class variable school_name. Print student details and school name. Change the school name using class name.

    Output:

        Enter student Name :
        somanath
        Enter Student Roll Number :
        252
        Enter the school name that you want to change :
        Marvellous Infosystem

        ------------Student Details-----------
        Name of student is        :  somanath
        Roll Number of Student is :  252
        School Name of Student is :  Marvellous Infosystem

'''
# Class Created
class Student:

    # Instance Calss Variable
    School_Name = 'Dr.J.J.M.C.O.E'

    # Constructor
    def __init__(self, name, roll_no):
        self.Name = name
        self.Roll_No = roll_no

    # Instance Method to display Student Details
    def studentDetails(self):
        print("------------Student Details-----------")
        print("Name of student is : ", self.Name)
        print("Roll Number of Student is : ", self.Roll_No)
        print("School Name of Student is : ", Student.School_Name)
        
# Main Function
def main():

    # Accept Name from User
    print("Enter student Name : ")
    sName = input()

    # Accept Roll Number from User
    print("Enter Student Roll Number : ")

    try:
        sRoll_No = int(input())
    except(ValueError):
        print("Invalid Input..! Enter Integer Values only..!")
        return
    
    # Accept school name from the user
    print("Enter the school name that you want to change : ")
    change_School = input()

    # Update the school name
    Student.School_Name = change_School
    
    # Object Created
    sobj = Student(sName, sRoll_No)

    # Instance Method Call
    sobj.studentDetails()

# Starter
if __name__ == "__main__":
    main()                  # Function call
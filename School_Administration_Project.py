# Note: It is assumed that the user enters the correct type of input each time
import csv

def write_into_file(data):
    file = open("Student_Information.csv", 'a')
    obj = csv.writer(file)
    if file.tell() == 0:  # if file is empty
        obj.writerow(["Name", "Age", "Grade", "Email"])
    obj.writerow(data)
    file.close()

run = True
student_count = 1

while run:
    info = input(f"Enter information for student {student_count} in the following format (Name Age Grade Email): ").split()
    print(f"The student info entered is \nName: {info[0]} \nAge: {info[1]} \nGrade: {info[2]} \nEmail: {info[3]}")
    verify = input("Is this information correct? (yes/no): ")
    if verify == 'yes':
        write_into_file(info)
        condition = input("Do you want to enter information for another student? (yes/no): ")
        if condition == 'yes':
            student_count += 1
        elif condition == 'no':
            run = False
    elif verify == 'no':
        run = "Please re-enter the information"

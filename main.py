import json
import os

a = int(input("Enter 1 for Admin; Enter 2 for Student\n"))
admin_data = []
student_data = []

if a == 1:
    admin_user = str(input("Adam Username: "))
    admin_passwd = str(input("Enter Adam_Password: "))

    path = 'C:/Users/David/Desktop/COMP1002/Group12_Project/'
    data_file = 'data.json'
    admin_data = {"admin_user": admin_user, "admin_passwd": admin_passwd}

    with open(os.path.join(path,data_file) ,'r') as file:
        data = json.load(file)

    data.append(admin_data)

    with open(data_file, 'w') as file:
        json.dump(data, file)


elif a == 2:
    student_user = input("Student Username: ")
    student_passwd = input("Enter Student_Password: ")
    student_data = [student_user, student_passwd]
    data_file = 'data.json'
    with open(data_file, 'w') as file:
        json.dump(student_data, file)





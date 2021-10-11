import os

a = int(input("Enter 1 for Admin; Enter 2 for Student\n"))
admin_data = []
student_data = []

if a == 1:
    admin_user = str(input("Adam Username: "))
    admin_passwd = str(input("Enter Adam_Password: "))

    data_file = 'C:/Users/David/Desktop/COMP1002/Group12_Project/admin_data.txt'
    #admin_data = str("admin_user", admin_user, " ", "admin_passwd", admin_passwd)

    with open(data_file, 'w') as f:
        f.write(admin_user + " " + admin_passwd)

elif a == 2:
    student_user = input("Student Username: ")
    student_passwd = input("Enter Student_Password: ")
    student_data = [student_user, student_passwd]
    data_file = 'C:/Users/David/Desktop/COMP1002/Group12_Project/student_data.txt'
    with open(data_file, 'w') as f:
        f.write(student_user + " " + student_passwd)






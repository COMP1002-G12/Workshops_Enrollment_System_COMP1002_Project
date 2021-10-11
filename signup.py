import os

a = int(input("Sign Up: Enter 1 for Admin; Enter 2 for Student\n"))

if a == 1:
    admin_user = str(input("Admin Username: "))
    admin_passwd = str(input("Enter Admin Password: "))

    data_file = f'C:/Users/David/Desktop/COMP1002/Group12_Project/{admin_user}.txt'

    #data_file = 'C:/Users/David/Desktop/COMP1002/Group12_Project/admin_data.txt'
    #admin_data = str("admin_user", admin_user, " ", "admin_passwd", admin_passwd)

    with open(data_file, 'w') as f:
        f.write(admin_passwd)

elif a == 2:
    student_user = str(input("Student Username: "))
    student_passwd = str(input("Enter Student_Password: "))
    
    #data_file = 'C:/Users/David/Desktop/COMP1002/Group12_Project/student_data.txt'
    data_file = f'C:/Users/David/Desktop/COMP1002/Group12_Project/{student_user}.txt'
    with open(data_file, 'w') as f:
        f.write(student_passwd)






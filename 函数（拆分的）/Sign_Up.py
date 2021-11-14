def Sign_Up(b):
    if b == 1:
        admin_user = str(input("Admin Username: "))
        admin_passwd = str(input("Enter Admin Password: "))

        data_file = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/GP/COMP1002_Group12_Project/admin/user/{admin_user}.txt'

        with open(data_file, 'w') as f:
            f.write(admin_passwd)
        
        return data_file

    elif b == 2:
        student_user = str(input("Student Username: "))
        student_passwd = str(input("Enter Student_Password: "))       
        
        data_file = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/GP/COMP1002_Group12_Project/student/{student_user}.txt'
        
        with open(data_file, 'w') as f:
            f.write(student_passwd)

        return data_file
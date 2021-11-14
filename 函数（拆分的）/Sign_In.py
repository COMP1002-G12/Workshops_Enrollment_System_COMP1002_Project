def Sign_In(c):
    if c == 1:
        admin_user = str(input("Admin Username: "))
        admin_passwd = str(input("Enter Admin Password: "))
        data_file = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/GP/COMP1002_Group12_Project/admin/user/{admin_user}.txt'

        with open(data_file) as f:
            contents = f.readline().splitlines()
            line1 = contents[0]

        while line1 != admin_passwd:
            print("Error to Login: Wrong Password.")
            admin_passwd = str(input("Enter Student Password: "))
        
        if line1 == admin_passwd:
            print("Successful into Workshop Enroll System ---Admin Account")
    
        return admin_user

    if c == 2:
        student_user_ID = str(input("Student ID: "))
        student_passwd = str(input("Enter Student Password: "))
        data_file = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/GP/COMP1002_Group12_Project/student/{student_user_ID}.txt'

        with open(data_file) as f:
            contents = f.readline().splitlines()
            line1 = contents[0]
            
        while line1 != student_passwd:
            print("Error to Login: Wrong Password.")
            student_passwd = str(input("Enter Student Password: "))

        if line1 == student_passwd:
            print("Successful into Workshop Enroll System ---Student Account", student_user_ID)
        
        return student_user_ID
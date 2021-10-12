import os


a = int(input('Enter 1 for sign up; Enter 2 for sign in:\n'))

if a == 1:

    b = int(input("Sign Up: Enter 1 for Admin; Enter 2 for Student\n"))

    if b == 1:
        admin_user = str(input("Admin Username: "))
        admin_passwd = str(input("Enter Admin Password: "))

        data_file = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/A_2/COMP1002_Group12_Project/admin/{admin_user}.txt'

        #data_file = 'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/A_2/COMP1002_Group12_Project/admin_data.txt'
        #admin_data = str("admin_user", admin_user, " ", "admin_passwd", admin_passwd)

        with open(data_file, 'w') as f:
            f.write(admin_passwd)

    elif b == 2:
        student_user = str(input("Student Username: "))
        student_passwd = str(input("Enter Student_Password: "))
        
        #data_file = 'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/A_2/COMP1002_Group12_Project/student_data.txt'
        data_file = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/A_2/COMP1002_Group12_Project/student/{student_user}.txt'
        with open(data_file, 'w') as f:
            f.write(student_passwd)

elif a == 2:
    c = int(input("Sign In: Enter 1 for Admin; Enter 2 for Student\n"))

    if c == 1:
        admin_user = str(input("Admin Username: "))
        admin_passwd = str(input("Enter Admin Password: "))
        data_file = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/A_2/COMP1002_Group12_Project/admin/{admin_user}.txt'

        with open(data_file) as f:
            contents = f.readline().splitlines()
            line1 = contents[0]

        if line1 == admin_passwd:
            print("Successful into Workshop Enroll System ---Admin Account")

        else:
            print("Error to Login: Wrong Password or User Name")


    if c == 2:
        student_user = str(input("Student Username: "))
        student_passwd = str(input("Enter Student Password: "))
        data_file = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/A_2/COMP1002_Group12_Project/student/{student_user}.txt'

        with open(data_file) as f:
            contents = f.readline().splitlines()
            line1 = contents[0]
        
#error:只能改密码但暂时无法改用户名
        while line1 != student_passwd:
            print("Error to Login: Wrong Password.")
            student_passwd = str(input("Enter Student Password: "))

        if line1 == student_passwd:
            print("Successful into Workshop Enroll System ---Student Account", student_user)

            d = int(input('Workshop: Enter 1 for sign up; Enter 2 for cancel:\n'))

            if d == 1:
                signup = str(input('Please give the number of the workshop which you want to sign up:'))
                print('Please check your choice:',end='')
                check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))
                log = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/A_2/COMP1002_Group12_Project/admin/log.txt'
                
                while check != 1:
                    signup = str(input('Please give the number of the workshop which you want to sign up again:'))
                    print('Please check your choice:',end='')
                    check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))

                with open(data_file,'a') as f:
                    f.write('\nThe choose of workshop:')
                    f.write(signup)

                with open(log,'a') as f:
                    f.write('The student name:')
                    f.write(student_user)
                    f.write('\tThe choose of workshop:')
                    f.write(signup)
                    f.write('\n')
                    
            
            elif d == 2:
                student_user = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/A_2/COMP1002_Group12_Project/student/{student_user}.txt'


                with open(student_user,'r') as f:
                    print('Your choice:')
                    data = f.readlines()              
                    print(''.join(data[1:]))
                    f.close

                cancel = int(input('Please give the number of the workshop which you want to cancel:'))
                print('Please check your choice:',end='')
                check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))
                
                while check != 1:
                    signup = str(input('Please give the number of the workshop which you want to cancel again:'))
                    print('Please check your choice:',end='')
                    check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))
                
                with open(student_user,'r') as f:
                    lines = f.readlines()
                with open(student_user, "w") as f:
                    for line in lines:
                        if line.strip("\n") != cancel:
                            f.write(line)
                



# def版，改善：去字母b,c...等，还需把input增加，函数可以在细化

# b = int(input("Sign Up: Enter 1 for Admin; Enter 2 for Student\n"))


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


# c = int(input("Sign In: Enter 1 for Admin; Enter 2 for Student\n"))


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
        student_user = str(input("Student Username: "))
        student_passwd = str(input("Enter Student Password: "))
        data_file = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/GP/COMP1002_Group12_Project/student/{student_user}.txt'

        with open(data_file) as f:
            contents = f.readline().splitlines()
            line1 = contents[0]
            
        while line1 != student_passwd:
            print("Error to Login: Wrong Password.")
            student_passwd = str(input("Enter Student Password: "))

        if line1 == student_passwd:
            print("Successful into Workshop Enroll System ---Student Account", student_user)
        
        return student_user


# d = int(input('Workshop: Enter 1 for sign up; Enter 2 for cancel:\n'))


def S1(student_user):
    signup = str(input('Please give the number of the workshop which you want to sign up:'))
    print('Please check your choice:',end='')
    check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))
    log = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/GP/COMP1002_Group12_Project/admin/document/log.txt'
        
    data_file = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/GP/COMP1002_Group12_Project/student/{student_user}.txt'
        
     
    while check != 1:
        signup = str(input('Please give the number of the workshop which you want to sign up again:'))
        print('Please check your choice:',end='')
        check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))

    with open(data_file,'a') as f:
        f.write('\n')
        f.write(student_user)
        f.write('\t')
        f.write(signup)

    with open(log,'a') as f:
        f.write('\n')
        f.write(student_user)
        f.write('\t')
        f.write(signup)

    return data_file,log                         
            
    
    

def S2(student_user):

    student_user = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/GP/COMP1002_Group12_Project/student/{student_user}.txt'
    log = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/GP/COMP1002_Group12_Project/admin/document/log.txt'


    with open(student_user,'r') as f:
        print('Your choice:')
        data = f.readlines()              
        print(''.join(data[1:]))
        f.close

    name = str(input('Please give your name:'))
    cancel = str(input('Please give the number of the workshop which you want to cancel:'))
    print('Please check your choice:',end='')
    check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))
                
    while check != 1:
        name = str(input('Please give your name:'))
        cancel = str(input('Please give the number of the workshop which you want to cancel:'))
        print('Please check your choice:',end='')
        check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))
                
    with open(student_user,'r') as f:
        lines = f.readlines()
                
    with open(student_user, "w") as f:
        for line in lines:
            if line.strip("\n") != name+'\t'+cancel:
                f.write(line)
                
    with open(log,'r') as f:
        lines = f.readlines()
                
    with open(log, "w") as f:
        for line in lines:
            if line.strip("\n") != name+'\t'+cancel:
                f.write(line)

        return student_user,log


# e = int(input('Authority: Enter 1 for adding; Enter 2 for cancel; Enter 3 for read:\n'))
# 这里可以去e


def Authority(e):
    if e == 1:
        student_name = str(input('Please give the name of the student:'))
        signup = str(input('Please give the number of the workshop which you want to add to student:'))
        log = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/GP/COMP1002_Group12_Project/admin/document/log.txt'                
        username = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/GP/COMP1002_Group12_Project/student/{student_name}.txt'
                    
        print('Please check your choice:',end='')
        check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))
                    
        while check != 1:
            signup = str(input('Please give the number of the workshop which you want to sign up again:'))
            print('Please check your choice:',end='')
            check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))
                    
        with open(username,'a') as f:
            f.write('\n')
            f.write(student_name)
            f.write('\t')
            f.write(signup)

        with open(log,'a') as f:
            f.write('\n')
            f.write(student_name)
            f.write('\t')
            f.write(signup)

    elif e == 2:
        log = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/GP/COMP1002_Group12_Project/admin/document/log.txt'

        with open(log,'r') as f:
            print('The log is:')
            data = f.readlines()              
            print(''.join(data))
            f.close                                
                
        student_name = str(input('Please give the name of the student:'))
        cancel = str(input('Please provide the workshop number of the student you want to cancel:'))
                
        username = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/GP/COMP1002_Group12_Project/student/{student_name}.txt'

        print('Please check your choice:',end='')
        check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))
                
        while check != 1:
            student_name = str(input('Please give the name of the student:'))
            cancel = str(input('Please give the number of the workshop which you want to cancel:'))
            print('Please check your choice:',end='')
            check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))
                
        with open(username,'r') as f:
            lines = f.readlines()
                
        with open(username, "w") as f:
            for line in lines:
                if line.strip("\n") != student_name+'\t'+cancel:
                    f.write(line)
                
        with open(log,'r') as f:
            lines = f.readlines()
                
        with open(log, "w") as f:
            for line in lines:
                if line.strip("\n") != student_name+'\t'+cancel:
                    f.write(line)

    elif e == 3:
        log = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/GP/COMP1002_Group12_Project/admin/document/log.txt'

        with open(log,'r') as f:
            print('The log is:')
            data = f.readlines()              
            print(''.join(data))
            f.close                                


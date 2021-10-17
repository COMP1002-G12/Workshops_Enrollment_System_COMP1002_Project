import os


a = int(input('Enter 1 for sign up; Enter 2 for sign in:\n'))


if a == 1:


    b = int(input("Sign Up: Enter 1 for Admin; Enter 2 for Student\n"))


    if b == 1:
        admin_user = str(input("Admin Username: "))
        admin_passwd = str(input("Enter Admin Password: "))

        data_file = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/A_2/COMP1002_Group12_Project/admin/user/{admin_user}.txt'

        with open(data_file, 'w') as f:
            f.write(admin_passwd)

    elif b == 2:
        student_user = str(input("Student Username: "))
        student_passwd = str(input("Enter Student_Password: "))       
        
        data_file = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/A_2/COMP1002_Group12_Project/student/{student_user}.txt'
        
        with open(data_file, 'w') as f:
            f.write(student_passwd)


elif a == 2:
    
    
    c = int(input("Sign In: Enter 1 for Admin; Enter 2 for Student\n"))


    if c == 1:
        admin_user = str(input("Admin Username: "))
        admin_passwd = str(input("Enter Admin Password: "))
        data_file = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/A_2/COMP1002_Group12_Project/admin/user/{admin_user}.txt'

        with open(data_file) as f:
            contents = f.readline().splitlines()
            line1 = contents[0]

        while line1 != admin_passwd:
            print("Error to Login: Wrong Password.")
            admin_passwd = str(input("Enter Student Password: "))
        
        if line1 == admin_passwd:
            print("Successful into Workshop Enroll System ---Admin Account")


            e = int(input('Authority: Enter 1 for adding; Enter 2 for cancel; Enter 3 for read:\n'))


            if e == 1:
                student_name = str(input('Please give the name of the student:'))
                signup = str(input('Please give the number of the workshop which you want to add to student:'))
 
                log = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/A_2/COMP1002_Group12_Project/admin/document/log.txt'                
                username = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/A_2/COMP1002_Group12_Project/student/{student_name}.txt'
                
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
                log = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/A_2/COMP1002_Group12_Project/admin/document/log.txt'

                with open(log,'r') as f:
                    print('The log is:')
                    data = f.readlines()              
                    print(''.join(data))
                    f.close                                
                
                student_name = str(input('Please give the name of the student:'))
                cancel = str(input('Please provide the workshop number of the student you want to cancel:'))
                
                username = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/A_2/COMP1002_Group12_Project/student/{student_name}.txt'

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
                log = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/A_2/COMP1002_Group12_Project/admin/document/log.txt'

                with open(log,'r') as f:
                    print('The log is:')
                    data = f.readlines()              
                    print(''.join(data))
                    f.close                                
# =======================================================================================
workshop_list = []
workshop_content = []
workshop_size = int(input('How many workshop you want to create:'))
n = input('please enter the action you want to do(input/storage/update/retrieval):')
if n == 'input':
    for i in range(workshop_size):
        workshop_list.append(input('please enter the title of the workshop:'))
        workshop_content.append(input('please enter the content and information of the workshop:'))
elif n == 'storage':

elif n == 'update':
    workshop_previous = input('enter the title of the workshop you want to update:')
    workshop_index = workshop_list.index(workshop_previous)
    workshop_list.remove(workshop_previous)
    workshop_content.remove(workshop_previous)
    workshop_update = input('enter the title you want to update:')
    workshop_list.insert(workshop_index,workshop_update)
    workshop_update_in_content = input('enter the information you want to update:')
    workshop_content.insert(workshop_index, workshop_update_in_content)

else:
    def sequential_search():
        workshop_retrieve: str = input('enter the title of the workshop you want to retrieve:')
        length = len(workshop_size)
        for i in range(length):
            if workshop_list[i] == workshop_retrieve:
                return i
            else:
                return False
# =======================================================================================
    if c == 2:
        student_user = str(input("Student Username: "))
        student_passwd = str(input("Enter Student Password: "))
        data_file = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/A_2/COMP1002_Group12_Project/student/{student_user}.txt'

        with open(data_file) as f:
            contents = f.readline().splitlines()
            line1 = contents[0]
        
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
                log = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/A_2/COMP1002_Group12_Project/admin/document/log.txt'
                
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
                                       
            
            elif d == 2:
                student_user = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/A_2/COMP1002_Group12_Project/student/{student_user}.txt'
                log = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/A_2/COMP1002_Group12_Project/admin/document/log.txt'


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
                        
                



def S1(student_user_ID):
    
    """ This part is for students to choose the workshop """
    data_file = f'./student/{student_user_ID}.txt'

    
    with open(data_file,'r') as f:
        print('Your choice:')
        data = f.readlines()              
        f.close
    s1 = ''.join(data[1:])
    l = s1.split()
    l1 = l[::2]
    l2 = l[1::2]                    
    l2 = list(map(int,l2))

    print('-' * 40)
    print("{0:^20}".format("Student_ID"),'|',"{0:^20}".format("Workshops"),sep='')
    print('-' * 40)
    l3 = []
    l4 = []
    for i in range(len(l2)):
        d1 = "{0:^20}".format(l1[i],l2[i])+'|'+"{1:^20}".format(l1[i],l2[i])
        l3.append(d1)
        l4.append(l2[i])
    l5 = sorted(l3)
    for i in l5:
        print(i)

    signup = str(input("Please give the number of the workshop which you want to sign up: "))
    while int(signup) in l4:
        print("You have chosen this workshop.")
        signup = str(input("Please give the number of the workshop which you want to sign up again: "))
    print("Please check your choice:",end="")
    check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))
    log = f'./admin/document/log.txt'
        
        
     
    while check != 1:
        signup = str(input("Please give the number of the workshop which you want to sign up again: "))
        while int(signup) in l4:
            print("You have chosen this workshop.")
            signup = str(input("Please give the number of the workshop which you want to sign up again: "))
        print("Please check your choice:",end="")
        check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))


    with open(data_file,'a') as f:
        f.write('\n')
        f.write(student_user_ID)
        f.write('\t')
        f.write(signup)

    with open(log,'a') as f:
        f.write('\n')
        f.write(student_user_ID)
        f.write('\t')
        f.write(signup)

                 
            
    
    

def S2(student_user_ID):

    """ This part is for students to cancel the selected workshop """

    data_file = f'./student/{student_user_ID}.txt'
    log = f'./admin/document/log.txt'

    with open(data_file,'r') as f:
        print('Your choice:')
        data = f.readlines()              
        f.close
    s1 = ''.join(data[1:])
    l = s1.split()
    l1 = l[::2]
    l2 = l[1::2]                    
    l2 = list(map(int, l2))

    print('-' * 40)
    print("{0:^20}".format("Student_ID"),'|',"{0:^20}".format("Workshops"),sep='')
    print('-' * 40)
    l3 = []
    l4 = []

    for i in range(len(l2)):
        d1 = "{0:^20}".format(l1[i],l2[i])+'|'+"{1:^20}".format(l1[i],l2[i])
        l3.append(d1)
        l4.append(l2[i])    
    l5 = sorted(l3)
    for i in l5:
        print(i)
    
    cancel = str(input("Please give the number of the workshop which you want to cancel: "))
    while int(cancel) not in l4:
        print("You haven't chosen this workshop.")
        cancel = str(input("Please give the number of the workshop which you want to cancel: "))
    print('Please check your choice:',end='')
    check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))
                
    while check != 1:
        cancel = str(input("Please give the number of the workshop which you want to cancel: "))
        while int(cancel) not in l4:
            print("You haven't chosen this workshop.")
            cancel = str(input("Please give the number of the workshop which you want to cancel: "))
        print('Please check your choice:',end='')
        check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))
                
    with open(data_file,'r') as f:
        lines = f.readlines()
                
    with open(data_file, "w") as f:
        for line in lines:
            if line.strip("\n") != student_user_ID+'\t'+cancel:
                f.write(line)
                
    with open(log,'r') as f:
        lines = f.readlines()
                
    with open(log, "w") as f:
        for line in lines:
            if line.strip("\n") != student_user_ID+'\t'+cancel:
                f.write(line)






def S3(student_user_ID):
    
    """ This part is for students to modify the Log_In password """

    data_file = f'./student/{student_user_ID}.txt'
    
    with open(data_file,'r') as f:
        contents = f.readline().splitlines()
        password0 = contents[0]
        f.close()

    password = str(input("Please enter the current password: "))
    while password != password0:
        print("The current password is incorrect, please re-enter.")
        password = str(input("Please enter the current password: "))
    
    if password == password0:
        print("The current password is correct.")
            

    password1 = str(input("Enter new Student_Password: "))
    password2 = str(input("Enter new Student_Password again: "))

    while password1 != password2:
        print("The password entered twice is different, please re-enter.")
        password1 = str(input("Enter new Student_Password: "))
        password2 = str(input("Enter new Student_Password again: "))

    while password0.strip("\n") == password1:
        print("Your password is the same, do you want to continue. Please check your choice:",end='')
        check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))

        if check == 1:
            break                     
        if check == 2:
            password1 = str(input("Enter new Student_Password: "))
            password2 = str(input("Enter new Student_Password again: "))

            while password1 != password2:
                print("The password entered twice is different, please re-enter.")
                password1 = str(input("Enter new Student_Password: "))
                password2 = str(input("Enter new Student_Password again: "))

    with open(data_file, "r") as f:
        lines = f.readlines()

    with open(data_file, "w") as f:
        f.write(password1)
        f.write('\n')
        for line in lines[1:]:
            f.write(line)

    print("Password modified successfully --- Student Account", student_user_ID)

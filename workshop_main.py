import os
import csv


def Sign_Up(b):

    """ This part is to register the workshop system """

    if b == 1:
        judge = False
        while not judge:

            admin_user = str(input("Admin Username: "))
            data_file = f'./admin/user/{admin_user}.txt'
            pathDir = os.listdir('./admin/user')
            T = admin_user + '.txt'

            if T in pathDir:
                print("Error! This Admin Account has been registered, please sign in or register a new account.")
            else:
                judge = True
                admin_passwd = str(input("Enter Admin Password: "))
                with open(data_file, 'w') as f:
                    f.write(admin_passwd)

    elif b == 2:
        judge = False
        while not judge:

            student_user_ID = str(input("Student User ID: "))
            data_file = f'./student/{student_user_ID}.txt'
            pathDir = os.listdir('./student')
            T = student_user_ID + '.txt'

            if T in pathDir:
                print("Error! This Student Account has been registered, please sign in or register a new account.")
            else:
                judge = True
                student_passwd = str(input("Enter Student_Password: "))
                with open(data_file, 'w') as f:
                    f.write(student_passwd)


def Log_In(c):

    """ This part is to log in to the workshop system """
    
    if c == 1:
        judge = False
        while not judge:
            
            admin_user = str(input("Admin Username: "))
            admin_passwd = str(input("Enter Admin Password: "))            
            data_file = f'./admin/user/{admin_user}.txt'
            pathDir = os.listdir('./admin/user')
            T = admin_user + '.txt'
            
            if T not in pathDir:
                print("Error! This Admin Account has not been registered yet, please enter correct account.")
            else:
                judge = True
                with open(data_file) as f:
                    contents = f.readline().splitlines()
                    line1 = contents[0]

                while line1 != admin_passwd:
                    print("Error to Login: Wrong Password.")
                    admin_passwd = str(input("Enter Student Password: "))
                
                if line1 == admin_passwd:
                    print("Successful into Workshop Enroll System --- Admin Account")
            

    if c == 2:
        judge = False
        while not judge:
            
            student_user_ID = str(input("Student ID: "))
            student_passwd = str(input("Enter Student Password: "))
            data_file = f'./student/{student_user_ID}.txt'
            pathDir = os.listdir('./student')
            T = student_user_ID + '.txt'
            
            if T not in pathDir:
                print("Error! This Student Account has not been registered yet, please enter correct account.")
            else:
                judge = True
                with open(data_file) as f:
                    contents = f.readline().splitlines()
                    line1 = contents[0]
                    
                while line1 != student_passwd:
                    print("Error to Login: Wrong Password.")
                    student_passwd = str(input("Enter Student Password: "))

                if line1 == student_passwd:
                    print("Successful into Workshop Enroll System --- Student Account", student_user_ID)
                
                return student_user_ID


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


def Authority(e):
    a = True
    while a:
        if e == 1:

            """ This part is for the administrator to help students choose the workshop """

            log = f'./admin/document/log.txt'
            with open(log,'r') as f:
                print("The log is:")
                data = f.readlines()[1:]
                f.close   

            s1 = ''.join(data)
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
                d1 = ("{0:^20}".format(l1[i],l2[i])+'|'+"{1:^20}".format(l1[i],l2[i]))
                d2 = l1[i],l2[i]
                l3.append(d1)
                l4.append(d2)
            l5 = sorted(l3)
            for i in l5:
                print(i)

            student_user_ID = str(input("Please give the ID of the student: "))
            signup = str(input("Please give the number of the workshop which you want to add to student: "))
            username = f'./student/{student_user_ID}.txt'
            d3 = (student_user_ID,int(signup))
            
            while d3 in l4:
                print("This student has chosen this workshop.")
                student_user_ID = str(input("Please give the ID of the student: "))
                cancel = str(input("Please provide the workshop number of the student you want to cancel: "))
                d3 = (student_user_ID,int(signup))
            print("Please check your choice:",end='')
            check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))

            while check != 1:
                student_user_ID = str(input("Please give the name of the student:"))
                cancel = str(input("Please give the number of the workshop which you want to cancel:"))
                d3 = (student_user_ID,int(signup))

                while d3 not in l4:
                    print("This student has chosen this workshop.")
                    student_user_ID = str(input("Please give the ID of the student: "))
                    cancel = str(input("Please provide the workshop number of the student you want to cancel: "))
                    d3 = (student_user_ID,int(signup))
                print("Please check your choice:",end='')
                check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))
                
            with open(username,'a') as f:
                f.write('\n')
                f.write(student_user_ID)
                f.write('\t')
                f.write(signup)

            with open(log,'a') as f:
                f.write('\n')
                f.write(student_user_ID)
                f.write('\t')
                f.write(signup)
            a = False
        elif e == 2:

            """ This part is for the administrator to cancel the workshop selected by the student """

            log = f'./admin/document/log.txt'

            with open(log,'r') as f:    
                        print("The log is:")
                        data = f.readlines()[1:]              
                        f.close   

            s1 = ''.join(data)
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
                d1 = ("{0:^20}".format(l1[i],l2[i])+'|'+"{1:^20}".format(l1[i],l2[i]))
                d2 = l1[i],l2[i]
                l3.append(d1)
                l4.append(d2)
            l5 = sorted(l3)
            for i in l5:
                print(i)

            student_user_ID = str(input("Please give the ID of the student: "))
            cancel = str(input("Please provide the workshop number of the student you want to cancel: "))
            username = f'。/student/{student_user_ID}.txt'
            d3 = (student_user_ID,int(cancel))
            
            while d3 not in l4:
                print("This student has not chosen this workshop.")
                student_user_ID = str(input("Please give the ID of the student: "))
                cancel = str(input("Please provide the workshop number of the student you want to cancel: "))
                d3 = (student_user_ID,int(cancel))
            print("Please check your choice:",end='')
            check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))

            while check != 1:
                student_user_ID = str(input("Please give the name of the student:"))
                cancel = str(input("Please give the number of the workshop which you want to cancel:"))
                d3 = (student_user_ID,int(cancel))

                while d3 not in l4:
                    print("This student has not chosen this workshop.")
                    student_user_ID = str(input("Please give the ID of the student: "))
                    cancel = str(input("Please provide the workshop number of the student you want to cancel: "))
                    d3 = (student_user_ID,int(cancel))
                print("Please check your choice:",end='')
                check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))
            
            
            with open(username,'r') as f:
                lines = f.readlines()

            with open(username, 'w') as f:
                for line in lines:
                    if line.strip("\n") != student_user_ID+'\t'+cancel:
                        f.write(line)

            with open(log,'r') as f:
                lines = f.readlines()

            with open(log, 'w') as f:
                for line in lines:
                    if line.strip("\n") != student_user_ID+'\t'+cancel:
                        f.write(line)
            a = False

        elif e == 3:
            
            """ This part is the administrator’s statistics on the workshop """

            log = f'./admin/document/log.txt'
            with open(log,'r') as f:    
                print("The log is:")
                data = f.readlines()[1:]              
                f.close   

            s1 = ''.join(data)
            l = s1.split()
            l1 = l[::2]
            l2 = l[1::2]                    
            l2 = list(map(int, l2))

            print('-' * 40)
            print("{0:^20}".format("Student_ID"),'|',"{0:^20}".format("Workshops"),sep='')
            print('-' * 40)
            l3 = []
            for i in range(len(l2)):
                d1 = ("{0:^20}".format(l1[i],l2[i])+'|'+"{1:^20}".format(l1[i],l2[i]))
                l3.append(d1)
            l4 = sorted(l3)
            for i in l4:
                print(i)
            
            while True:
                choose = int(input("Enter 1 for inputing the workshop number to know who chose this workshop; Enter 2 for inputing student_ID to know which workshops are selected:\n"))
            
                if choose == 1:
                    v = int(input("Enter the workshop number to know who chose this workshop: "))
                    l = []
                    for i in range(len(l2)):
                        d1 = {l1[i]:l2[i]}

                        for key,val in d1.items():
                            if val == v:
                                l += [key]
                    if l == []:
                        print("No student has chosen this workshop yet.")
                    else:
                        print("These student_IDs chose this workshop:\n",sorted(l))

                elif choose == 2:
                    k = str(input("Enter student_ID to know which workshops are selected: "))
                    l = []
                    for i in range(len(l2)):
                        d1 = {l1[i]:l2[i]}

                        for key,val in d1.items():
                            if key == k:
                                l += [val]    
                    if l == []:
                        print("No student has chosen this workshop yet.")
                    else:
                        print("These student_IDs chose this workshop:\n",sorted(l))
                elif choose == 3:
                    a = False
                    break

        elif e == 4:
            
            """ This part can reset the student's Log_In password """
            
            student_user_ID = str(input("Please give the ID of the student: "))
            username = f'./student/{student_user_ID}.txt'
            change = int(input("Change the password: Enter 1 to reset password; Enter 2 to quit:\n"))

            if change == 1:
                password1 = '20345678'

                with open(username, "r") as f:
                    lines = f.readlines()

                with open(username, "w") as f:
                    f.write(password1)
                    f.write('\n')
                    for line in lines[1:]:
                        f.write(line)

                print("Password reseted successfully --- Student Account", student_user_ID)
                a = False
            elif change == 2:
                a = False

        elif e == 5:
            break


print("*" * 35)
print("*" + " " * 33 + "*")
print("*" + " " * 33 + "*")
print("*" + " --Workshops Enrollment System-- " + "*")
print("*" + "                    --- Group 12 " + "*")
print("*" + " " * 33 + "*")
print("*" + " " * 33 + "*")
print("*" + " " * 33 + "*")
print("*" * 35)


while True:
    a = int(input('Enter 1 for sign up; Enter 2 for sign in; Enter 3 for quit; Enter 4 for About:\n'))
    if a == 1:
        b = int(input("Sign Up: Enter 1 for Admin; Enter 2 for Student\n"))
        Sign_Up(b)
    elif a == 2:
        c = int(input("Sign In: Enter 1 for Admin; Enter 2 for Student\n"))
        ID = Log_In(c)
        if c == 1:
            D = {1:"Add workshop for student",2:"Cancel workshop for student",3:"Read the workshop",4:"Reset the student's Log_In password"}
            print("{0:^10}".format("Number"),'|',"{0:^50}".format("Function"))
            print("-"*60)
            for k,v in D.items():
                print("{0:^10}".format(k),'|',"{0:}".format(v))
            e = int(input('Enter the number:\n'))
            Authority(e)
        if c == 2:
            f = True
            while f:
                d = int(input('Enter 1 for sign up workshop; Enter 2 for cancel workshop; Enter 3 for change password:\n'))
                if d == 1:
                    S1(ID)
                 
                elif d == 2:
                    S2(ID)
                    
                elif d == 3:
                    S3(ID)
                    
                elif d == 4:
                    f = False
    elif a == 3:
        break
    elif a == 4:
        print("*" * 41)
        print("*" + " " * 15 + "--About--" + " " * 15 + "*")
        print("*" + " " * 39 + "*")
        print("*" + " Name: Workshops Enrollment System     " + "*")
        print("*" + " Production team: COMP1002 Group 12    " + "*")
        print("*" + " " * 39 + "*")
        print("*" + " Members:" + " " * 30 + "*")
        print("*" + " JIANG Guanlin (21093962d)" + " " * 13 + "*")
        print("*" + " LIU Minghao (21096308d)" + " " * 15 + "*")
        print("*" + " CHEN Ziyang (21095751d)" + " " * 15 + "*")
        print("*" + " HE Boyan (21096184d)" + " " * 18 + "*")
        print("*" + " " * 39 + "*")
        print("*" + "Software Copyright© belongs to Group 12" + "*")
        print("*" + " " * 39 + "*")
        print("*" * 41)



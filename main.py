import os
import csv

def Sign_Up(b):

    """ This part is to register the workshop system """

    if b == 1:
        judge = False
        while not judge:

            admin_user = str(input("Admin Username: "))
            admin_user = admin_user.lower()
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
            student_user_ID = student_user_ID.lower()
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
            admin_user = admin_user.lower()
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
                    print("Successful into Workshop Enrollment System --- Admin Account")
            

    if c == 2:
        judge = False
        while not judge:
            
            student_user_ID = str(input("Student ID: "))
            student_user_ID = student_user_ID.lower()
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
                    print("Successful into Workshop Enrollment System --- Student Account", str(student_user_ID).upper())
                
                return student_user_ID


def judgement2(workshop_list1,signup):
    controller = True
    for i in range(len(workshop_list1)):
        if controller:
            if signup == workshop_list1[i][1] and int(workshop_list1[i][4]) > 0:
                controller = False
    return controller


def S1(student_user_ID):
    
    """ This part is for students to choose the workshop """

    log = f'./admin/document/log.txt'
    data_file = f'./student/{student_user_ID}.txt'
    workshop_csv = f'./admin/document/workshop.csv'
    workshop_list1 = []

    with open(workshop_csv, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file.close()

    for line in lines:
        workshop_content = line.split(',')
        workshop_list1.append(workshop_content)
    
    print()
    print("This is the list of workshops:")
    field_names = ['Index', 'Workshop_ID', 'Workshop_Name', 'Total','Remain']
    print('-' * 104)
    print('{0:^20}'.format(field_names[0]), '|', '{0:^20}'.format(field_names[1]),'|','{0:^20}'.format(field_names[2]),'|','{0:^20}'.format(field_names[3]),'|','{0:^20}'.format(field_names[4]),sep='')
    print('-' * 104)
    for line in lines:
        workshop_content = line.split(',')
        print('{0:^20}'.format(workshop_content[0]), '|', '{0:^20}'.format(workshop_content[1]),'|','{0:^20}'.format(workshop_content[2]), '|','{0:^20}'.format(workshop_content[3]), '|','{0:^20}'.format(workshop_content[4][0:-1]), sep='')

    ask = int(input("Enter 1 for Read Workshop Description; Enter 2 for Skip: "))
    if ask == 1:
        student_check_ws()
    elif ask == 2:
        pass

    with open(data_file,'r') as f:
        print()
        print('Your choice:')
        data = f.readlines()              
        f.close

    s1 = ''.join(data[1:])
    l = s1.split()
    l1 = l[::2]
    l2 = l[1::2]                    
    l2 = list(map(int,l2))

    if l1 == l2 == []:
        print("* You haven't chosen any workshop.")
        l4 = []
        for i in range(len(l2)):
            l4.append(l2[i])
    else:
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


    signup = str(input('Please give the ID of the workshop which you want to sign up(Enter "Q" or "q" to select again): '))
    if signup.lower() == "q":
        return
    else:
        while int(signup) in l4:
            print("You have chosen this workshop.")
            signup = str(input("Please give the number of the workshop which you want to sign up again: "))

        while judgement2(workshop_list1,signup):
            print("There is no remaining in this workshop.")
            signup = str(input("Please give the number of the workshop which you want to sign up: "))

        print("Please check your choice:",end="")
        check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))

        while check != 1:
            signup = str(input("Please give the number of the workshop which you want to sign up again: "))
            
            while int(signup) in l4:
                print("You have chosen this workshop.")
                signup = str(input("Please give the number of the workshop which you want to sign up again: "))       

            while (workshop_list1,signup):
                print("There is no remaining in this workshop.")
                signup = str(input("Please give the number of the workshop which you want to sign up: "))

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

        with open(workshop_csv, 'w', encoding='utf-8', newline='') as file:
            for b in workshop_list1:
                if signup != b[1]:
                    c = [str(int(b[0])), str(b[1]), str(b[2]),str(b[3]),str(b[4][:-1])]
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(c)
                else:
                    c = [str(int(b[0])), str(b[1]), str(b[2]),str(b[3]),str(int(b[4][:-1])-1)]
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(c)

        print("Enroll the workshop successfully --- Student Account", str(student_user_ID).upper())


def S2(student_user_ID):

    """ This part is for students to cancel the selected workshop """

    data_file = f'./student/{student_user_ID}.txt'
    log = f'./admin/document/log.txt'
    workshop_csv = f'./admin/document/workshop.csv'
    workshop_list1 = []

    with open(data_file,'r') as f:
        print()
        print('Your choice:')
        data = f.readlines()              
        f.close

    s1 = ''.join(data[1:])
    l = s1.split()
    l1 = l[::2]
    l2 = l[1::2]                    
    l2 = list(map(int, l2))

    if l1 == l2 == []:
        print("* You haven't chosen any workshop. Please choose workshop first.")
        return
    else:
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

    cancel = str(input('Please give the number of the workshop which you want to cancel(Enter "Q" or "q" to select again): '))
    if cancel.lower() == "q":
        return
    else:
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

        with open(workshop_csv, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            file.close()

        for line in lines:
            workshop_content = line.split(',')
            workshop_list1.append(workshop_content)

        with open(workshop_csv, 'w', encoding='utf-8', newline='') as file:
            for b in workshop_list1:
                if cancel != b[1]:
                    c = [str(int(b[0])), str(b[1]), str(b[2]),str(b[3]),str(b[4][:-1])]
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(c)
                else:
                    c = [str(int(b[0])), str(b[1]), str(b[2]),str(b[3]),str(int(b[4][:-1])+1)]
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(c)

        print("Cancel the workshop successfully --- Student Account", str(student_user_ID).upper())


def S3(student_user_ID):
    data_file = f'./student/{student_user_ID}.txt'
    workshop_csv = f'./admin/document/workshop.csv'
    workshop_list1 = []
    
    with open(workshop_csv, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file.close()

    for line in lines:
        workshop_content = line.split(',')
        workshop_list1.append(workshop_content)
    
    print()
    print("This is the list of workshops:")
    field_names = ['Index', 'Workshop_ID', 'Workshop_Name', 'Total','Remain']
    print('-' * 104)
    print('{0:^20}'.format(field_names[0]), '|', '{0:^20}'.format(field_names[1]),'|','{0:^20}'.format(field_names[2]),'|','{0:^20}'.format(field_names[3]),'|','{0:^20}'.format(field_names[4]),sep='')
    print('-' * 104)
    for line in lines:
        workshop_content = line.split(',')
        print('{0:^20}'.format(workshop_content[0]), '|', '{0:^20}'.format(workshop_content[1]),'|','{0:^20}'.format(workshop_content[2]), '|','{0:^20}'.format(workshop_content[3]), '|','{0:^20}'.format(workshop_content[4][0:-1]), sep='')

    with open(data_file,'r') as f:
        print()
        print('Your choice:')
        data = f.readlines()              
        f.close

    s1 = ''.join(data[1:])
    l = s1.split()
    l1 = l[::2]
    l2 = l[1::2]                    
    l2 = list(map(int, l2))

    if l1 == l2 == []:
        print("* You haven't chosen any workshop. Please choose workshop first.")
        return
    else:
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
    print()
    ask = int(input("Enter 1 for Read Workshop Description; Enter 2 for Skip: "))
    if ask == 1:
        student_check_ws()
    elif ask == 2:
        pass


def S4(student_user_ID):
    
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


def student_check_ws():
    workshop_id = input("Enter the Workshop ID: ")
    desc_file = workshop_id + ".txt"
    file_dir = "./admin/document/workshop/"
    file = file_dir + desc_file
    
    with open(file, "r") as f:
        content = f.readlines()
    print()
    print("Description: " + ''.join(content))


def Student(d,ID):
    a = True
    if d == 1:
        S1(ID)
        return a
    elif d == 2:
        S2(ID)
        return a
    elif d == 3:
        S3(ID)
        b = str(input('Enter "Q" or "q" to exit: '))
        return a
    elif d == 4:
        S4(ID)
        return a
    elif d == 4:
        a = False
        return a


def judgement1(workshop_list1,workshop):
    controller = True
    for i in range(len(workshop_list1)):
        if controller:
            if workshop == workshop_list1[i][2]:
                controller = False
    return controller


def judgement3(workshop_list1,workshop_ID,workshop_name):
    controller = True
    for i in range(len(workshop_list1)):
        if controller:
            if str(workshop_ID) == workshop_list1[i][1] and workshop_name == workshop_list1[i][2]:
                controller = False
    return controller


def judgement4(workshop_list1,workshop):
    controller = True
    for i in range(len(workshop_list1)):
        if controller:
            if workshop in workshop_list1[i]:
                controller = False
    return controller


def judgement5(workshop_list1,workshop):
    controller = True
    for i in range(len(workshop_list1)):
        if controller:
            if workshop == workshop_list1[i][1]:
                controller = False
    return controller


def update_workshop():
    workshop_list1 = []
    workshop_csv = f'./admin/document/workshop.csv'    

    with open(workshop_csv, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file.close()
    
    if lines == []:
        print("* No workshop yet. Please add workshop first.")
        return
    else:
        field_names = ['Index', 'Workshop_ID', 'Workshop_Name', 'Total','Remain']
        print('-' * 104)
        print(
        '{0:^20}'.format(field_names[0]), '|', '{0:^20}'.format(field_names[1]), '|', '{0:^20}'.format(field_names[2]), '|',
        '{0:^20}'.format(field_names[3]),'|','{0:^20}'.format(field_names[4]),sep='')
        print('-' * 104)
        for line in lines:
            workshop_content = line.split(',')
            print('{0:^20}'.format(workshop_content[0]), '|', '{0:^20}'.format(workshop_content[1]), '|',
                '{0:^20}'.format(workshop_content[2]), '|','{0:^20}'.format(workshop_content[3]), '|','{0:^20}'.format(workshop_content[4][0:-1]), sep='')
    
    for line in lines:
        workshop_content = line.split(',')
        workshop_list1.append(workshop_content)
    
    workshop_ID = str(input("Please enter current workshop ID: "))
    workshop_name = str(input("Please enter current workshop name: "))
    
    while judgement3(workshop_list1,workshop_ID,workshop_name):
        print("The entered workshop_ID does not match the workshop_name.")
        workshop_ID = str(input("Please enter current workshop ID: "))
        workshop_name = str(input("Please enter current workshop name: "))    

    workshop_des = f'./admin/document/workshop/{workshop_ID}.txt'

    z = True
    while z:
        D1 = {1:"Change 'Workshop_Name'",2:"Change 'Total'",3:"Change Description",4:"Exit"}
        print("-"*35)
        print("{0:^10}".format("Number"),'|',"{0:^20}".format("Function"))
        print("-"*35)
        for k,v in D1.items():
            print("{0:^10}".format(k),'|',"{0:}".format(v))
        n = int(input('Enter the number:\n'))
        if n == 1:
            workshop_newName = str(input("Please enter a new workshop name: "))
                
            while not judgement1(workshop_list1,workshop_newName):
                print("The list have this workshop.")
                workshop_newName = str(input("Please enter a new workshop name: "))

            with open(workshop_csv, 'w', encoding='utf-8', newline='') as file:

                for b in workshop_list1:
                    if workshop_name == b[2] and str(workshop_ID) == b[1]:
                        c = [str(int(b[0])), str(b[1]), workshop_newName,str(b[3]),str(b[4][:-1])]     
                        csv_writer = csv.writer(file)
                        csv_writer.writerow(c)
                    else:
                        c = [str(int(b[0])), str(b[1]), str(b[2]),str(b[3]),str(b[4][:-1])]     
                        csv_writer = csv.writer(file)
                        csv_writer.writerow(c)

                file.close()
            print('The workshop with ID',workshop_ID,'has successfully changed its name.')
            
            with open(workshop_csv, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                file.close()
            print('-' * 104)
            print(
            '{0:^20}'.format(field_names[0]), '|', '{0:^20}'.format(field_names[1]), '|', '{0:^20}'.format(field_names[2]), '|',
            '{0:^20}'.format(field_names[3]),'|','{0:^20}'.format(field_names[4]),sep='')
            print('-' * 104)
            for line in lines:
                workshop_content = line.split(',')
                print('{0:^20}'.format(workshop_content[0]), '|', '{0:^20}'.format(workshop_content[1]), '|',
                    '{0:^20}'.format(workshop_content[2]), '|','{0:^20}'.format(workshop_content[3]), '|','{0:^20}'.format(workshop_content[4][0:-1]), sep='')

            z = False

        elif n == 2:
            workshop_total = int(input('Please enter a new total number of students accommodated: '))

            with open(workshop_csv, 'w', encoding='utf-8', newline='') as file:

                for b in workshop_list1:
                    if workshop_name == b[2] and str(workshop_ID) == b[1]:
                        c = [str(int(b[0])), str(b[1]),str(b[2]),str(workshop_total),str(workshop_total-(int(b[3])-int(b[4][:-1])))]     
                        csv_writer = csv.writer(file)
                        csv_writer.writerow(c)
                    else:
                        c = [str(int(b[0])), str(b[1]), str(b[2]),str(b[3]),str(b[4][:-1])]     
                        csv_writer = csv.writer(file)
                        csv_writer.writerow(c)
                
                file.close()
            print('The workshop with ID',workshop_ID,'has successfully changed its total.')
            
            with open(workshop_csv, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                file.close()
            print('-' * 104)
            print(
            '{0:^20}'.format(field_names[0]), '|', '{0:^20}'.format(field_names[1]), '|', '{0:^20}'.format(field_names[2]), '|',
            '{0:^20}'.format(field_names[3]),'|','{0:^20}'.format(field_names[4]),sep='')
            print('-' * 104)
            for line in lines:
                workshop_content = line.split(',')
                print('{0:^20}'.format(workshop_content[0]), '|', '{0:^20}'.format(workshop_content[1]), '|',
                    '{0:^20}'.format(workshop_content[2]), '|','{0:^20}'.format(workshop_content[3]), '|','{0:^20}'.format(workshop_content[4][0:-1]), sep='')

            z = False
        
        elif n == 3:
            with open(workshop_des,'r') as f:
                lines = f.readlines()

            desc = str(input("Please enter new Description: "))
            lines[0] = desc+'\n'

            with open(workshop_des,'w') as f:
                for line in lines:
                    f.write(line)
                f.close()

            z = False
        
        elif n == 4:
            z = False


def delete_workshop():
    workshop_list1 = []
    log = f'./admin/document/log.txt'
    workshop_csv = f'./admin/document/workshop.csv'    
    with open(workshop_csv, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file.close()
    if lines == []:
        print("* No workshop yet. Please add workshop first.")
        return
    else:
        field_names = ['Index', 'Workshop_ID', 'Workshop_Name', 'Total','Remain']
        print('-' * 104)
        print(
        '{0:^20}'.format(field_names[0]), '|', '{0:^20}'.format(field_names[1]), '|', '{0:^20}'.format(field_names[2]), '|',
        '{0:^20}'.format(field_names[3]),'|','{0:^20}'.format(field_names[4]),sep='')
        print('-' * 104)
        for line in lines:
            workshop_content = line.split(',')
            print('{0:^20}'.format(workshop_content[0]), '|', '{0:^20}'.format(workshop_content[1]), '|',
                '{0:^20}'.format(workshop_content[2]), '|','{0:^20}'.format(workshop_content[3]), '|','{0:^20}'.format(workshop_content[4][0:-1]), sep='')
    for line in lines:
        workshop_content = line.split(',')
        workshop_list1.append(workshop_content)
    
    workshop_ID = str(input('Please enter the workshop ID(Enter "Q" or "q" to select again): '))
    if workshop_ID.lower() == "q":
        return
    else:
        while judgement5(workshop_list1,workshop_ID):
            print("The list does not have this workshop.")
            workshop_ID = str(input("Please enter the workshop name: "))
        
        for b in workshop_list1:
            if workshop_ID == b[1]:
                a = int(b[0])

        with open(workshop_csv, 'w', encoding='utf-8', newline='') as file:

            for b in workshop_list1:
                if workshop_ID != b[1]:
                    if int(b[0]) > a:
                        c = [str(int(b[0]) - 1), str(b[1]), str(b[2]),str(b[3]), str(b[4][:-1])]
                        csv_writer = csv.writer(file)
                        csv_writer.writerow(c)
                    else:
                        c = [str(int(b[0])), str(b[1]), str(b[2]),str(b[3]),str(b[4][:-1])]
                        csv_writer = csv.writer(file)
                        csv_writer.writerow(c)

        ws_desc_file = f'./admin/document/workshop/{workshop_ID}.txt'
        os.remove(ws_desc_file)
        
        with open(workshop_csv, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            file.close()
        print('-' * 104)
        print(
        '{0:^20}'.format(field_names[0]), '|', '{0:^20}'.format(field_names[1]), '|', '{0:^20}'.format(field_names[2]), '|',
        '{0:^20}'.format(field_names[3]),'{0:^20}'.format(field_names[4]),sep='')
        print('-' * 104)
        for line in lines:
            workshop_content = line.split(',')
            print('{0:^20}'.format(workshop_content[0]), '|', '{0:^20}'.format(workshop_content[1]), '|',
                '{0:^20}'.format(workshop_content[2]), '|','{0:^20}'.format(workshop_content[3]), '|','{0:^20}'.format(workshop_content[4][0:-1]), sep='')


        with open(log,'r') as f:
            data = f.readlines()
            f.close   

        s1 = ''.join(data)
        l = s1.split()
        l1 = l[::2]
        l2 = l[1::2]
        l2 = list(map(int, l2))
        if l1 == l2 == []:
            pass
        else:
            l4 = []
            for i in range(len(l2)):
                if int(workshop_ID) == l2[i]:
                    l4.append(l1[i])
        
            if l4 == []:
                return
            else:
                for c in l4:
                    with open(log,'r') as f:
                        lines = f.readlines()

                    with open(log, 'w') as f:
                        for line in lines:
                            if line.strip("\n") != c+'\t'+workshop_ID:
                                f.write(line)
                    
                    username = f'./student/{c}.txt'

                    with open(username,'r') as f:
                        lines = f.readlines()

                    with open(username, 'w') as f:
                        for line in lines:
                            if line.strip("\n") != c+'\t'+workshop_ID:
                                f.write(line)


def retrieve_workshop():
    workshop_csv = f'./admin/document/workshop.csv'    
    workshop_list1 = []
    with open(workshop_csv, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file.close()
    if lines == []:
        print("* No workshop yet. Please add workshop first.")
        return
    else:
        field_names = ['Index', 'Workshop_ID', 'Workshop_Name', 'Total','Remain']
        print('-' * 104)
        print(
        '{0:^20}'.format(field_names[0]), '|', '{0:^20}'.format(field_names[1]), '|', '{0:^20}'.format(field_names[2]), '|',
        '{0:^20}'.format(field_names[3]),'|','{0:^20}'.format(field_names[4]),sep='')
        print('-' * 104)
        for line in lines:
            workshop_content = line.split(',')
            print('{0:^20}'.format(workshop_content[0]), '|', '{0:^20}'.format(workshop_content[1]), '|',
                '{0:^20}'.format(workshop_content[2]), '|','{0:^20}'.format(workshop_content[3]), '|','{0:^20}'.format(workshop_content[4][0:-1]), sep='')

    workshop = str(input("Please enter the name or ID of the workshop you want to find: "))

    for line in lines:
        workshop_content = line.split(',')
        workshop_list1.append(workshop_content)

    while judgement4(workshop_list1,workshop):
        print("The list does not have this workshop.")
        workshop = str(input("Please enter the name or ID of the workshop you want to find: "))

    find_name = ["Workshop_ID","Workshop_Name","Total","Remain"]
    print("This is the information for this course:")
    print('-' * 84)
    print('{0:^20}'.format(find_name[0]), '|', '{0:^20}'.format(find_name[1]), '|',
    '{0:^20}'.format(find_name[2]),'|','{0:^20}'.format(find_name[3]),sep='')
    print('-' * 84)
    for b in workshop_list1:
        if workshop == b[1] or workshop == b[2]:
            print('{0:^20}'.format(b[1]), '|', '{0:^20}'.format(b[2]), '|','{0:^20}'.format(b[3]),'|','{0:^20}'.format(b[4][0:-1]), sep='')
    
    print()
    ask = int(input("Enter 1 for Read Workshop Description; Enter 2 for Skip: "))
    if ask == 1:
        student_check_ws()
        print()
    elif ask == 2:
        pass


def storage_workshop():
    workshop_csv = f'./admin/document/workshop.csv'        
    workshop_list = []
    workshop_content = []
    print("Please do not enter more than 20 letters:")
    with open (workshop_csv,'r',encoding='utf-8') as file:
        lines = file.readlines()
    if lines == []:
        print("* No workshop yet. Please add workshop first.")
    else:
        field_names = ['Index','Workshop_ID','Workshop_Name','Total','Remain']

        print('-'*104)
        print('{0:^20}'.format(field_names[0]),'|','{0:^20}'.format(field_names[1]),'|','{0:^20}'.format(field_names[2]),'|','{0:^20}'.format(field_names[3]),'|','{0:^20}'.format(field_names[4]),sep='')
        print('-'*104)
        for line in lines:
            workshop_content = line.split(',')
            print('{0:^20}'.format(workshop_content[0]),'|','{0:^20}'.format(workshop_content[1]),'|','{0:^20}'.format(workshop_content[2]),'|','{0:^20}'.format(workshop_content[3]),'|','{0:^20}'.format(workshop_content[4][0:-1]),sep='')

    judge = False
    while not judge:
        with open (workshop_csv,'r',encoding='utf-8') as file:
            lines = file.readlines()
            file.close()

        length = len(lines)
        workshop_ID = str(input("Please enter the ID of the workshop: "))
        workshop_name = str(input("Please enter the workshop name: "))

        for line in lines:
            workshop_content = line.split(',')
            workshop_list.append(workshop_content)

        for b in workshop_list:
            while workshop_name in b[2] or str(workshop_ID) in b[1]:
                print("There is already a workshop with the same ID or name, please change the ID or name: ")
                workshop_ID = str(input("Please enter the ID of the workshop: "))
                workshop_name = str(input("Please enter the workshop name: "))

        remain = total = int(input("Please enter the total number of students: "))
        remind = int(input("Enter 1 for Continue, Enter 2 for Quit: "))

        if remind == 1:
            Index = length + 1
            data = [str(Index),str(workshop_ID),workshop_name,str(total),str(remain)]
            with open(workshop_csv,'a',encoding='utf-8',newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(data) 
            file.close()

        elif remind == 2:
            judge = True
            Index = length + 1
            data = [str(Index),str(workshop_ID),workshop_name,str(total),str(remain)]
            with open(workshop_csv,'a',encoding='utf-8',newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(data) 
            file.close()

    with open (workshop_csv,'r',encoding='utf-8') as file:
        lines = file.readlines()

    field_names = ['Index','Workshop_ID','Workshop_Name','Total','Remain']

    print('-'*104)
    print('{0:^20}'.format(field_names[0]),'|','{0:^20}'.format(field_names[1]),'|','{0:^20}'.format(field_names[2]),'|','{0:^20}'.format(field_names[3]),'|','{0:^20}'.format(field_names[4]),sep='')
    print('-'*104)
    for line in lines:
        workshop_content = line.split(',')
        print('{0:^20}'.format(workshop_content[0]),'|','{0:^20}'.format(workshop_content[1]),'|','{0:^20}'.format(workshop_content[2]),'|','{0:^20}'.format(workshop_content[3]),'|','{0:^20}'.format(workshop_content[4][0:-1]),sep='')


def ws_description():

    workshop_csv = f"./admin/document/workshop.csv"

    with open (workshop_csv,'r',encoding='utf-8') as file:
        lines = file.readlines()
    if lines == []:
        print("* No workshop yet. Please add workshop first.")
        return
    else:
        field_names = ['Index','Workshop_ID','Workshop_Name','Total','Remain']

        print('-'*104)
        print('{0:^20}'.format(field_names[0]),'|','{0:^20}'.format(field_names[1]),'|','{0:^20}'.format(field_names[2]),'|','{0:^20}'.format(field_names[3]),'|','{0:^20}'.format(field_names[4]),sep='')
        print('-'*104)
        for line in lines:
            workshop_content = line.split(',')
            print('{0:^20}'.format(workshop_content[0]),'|','{0:^20}'.format(workshop_content[1]),'|','{0:^20}'.format(workshop_content[2]),'|','{0:^20}'.format(workshop_content[3]),'|','{0:^20}'.format(workshop_content[4][0:-1]),sep='')

        i_ID = int(input("Enter the Workshop ID for Description need: "))
        for line in lines:
            workshop_content = line.split(',')
            if int(workshop_content[1]) == i_ID:
                desc = input(workshop_content[2] + "--- Description: ")
                desc_file = f'./admin/document/workshop/{workshop_content[1]}.txt'
                with open(desc_file, 'w') as f:
                        f.write(desc)


def reset_password():
    
    """ This part can reset the student's Log_In password """
            
    student_user_ID = str(input("Please give the ID of the student: "))
    student_user_ID = student_user_ID.lower()
    username = f'./student/{student_user_ID}.txt'
    change = int(input("Choose: Enter 1 to reset password; Enter 2 to quit:\n"))

    if change == 1:
        password1 = '12345678'

        with open(username, "r") as f:
            lines = f.readlines()

        with open(username, "w") as f:
            f.write(password1)
            f.write('\n')
            for line in lines[1:]:
                f.write(line)
        print("Password reseted successfully --- Student Account", student_user_ID)                
    elif change == 2:
        print("Quit successfully.")


def retrieve_log():
    
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
    if l1 == l2 == []:
        print("* No students choose workshop yet.")
    else:
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
        choose = {1:"Input the workshop number to know who chose this workshop",2:"Input student_ID to know which workshops are selected",3:"Quit"}
        print()
        print()
        print("-"*75)
        print("{0:^10}".format("Number"),'|',"{0:^65}".format("Function"))
        print("-"*75)
        for k,v in choose.items():
            print("{0:^10}".format(k),'|',"{0:}".format(v))
        n_choose = int(input('Enter the number:\n'))

        if n_choose == 1:
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

        elif n_choose == 2:
            k = str(input("Enter student_ID to know which workshops are selected: "))
            l = []
            for i in range(len(l2)):
                d1 = {l1[i]:l2[i]}

                for key,val in d1.items():
                    if key == k:
                        l += [val]    
            if l == []:
                print("This student hasn't chosen workshop yet.")
            else:
                print("This student chose these workshops:\n",sorted(l))
        elif n_choose == 3:
            break


def cancel_Sworkshop():
    
    """ This part is for the administrator to cancel the workshop selected by the student """
    workshop_csv = f'./admin/document/workshop.csv'
    log = f'./admin/document/log.txt'
    workshop_list1 = []
    with open(log,'r') as f:    
        print("The log is:")
        data = f.readlines()[1:]              
        f.close   

    s1 = ''.join(data)
    l = s1.split()
    l1 = l[::2]
    l2 = l[1::2]                    
    l2 = list(map(int, l2))
    if l1 == l2 == []:
        print("* No students choose workshop yet.")
    else:
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

    student_user_ID = str(input('Please give the ID of the student(Enter "Q" or "q" to exit): '))
    student_user_ID = student_user_ID.lower()
    if student_user_ID == 'q':
        return
    else:
        l = []
        for i in range(len(l2)):
            d1 = {l1[i]:l2[i]}

            for key,val in d1.items():
                if key == student_user_ID:
                    l += [val]    
        if l == []:
            print("This student hasn't chosen workshop yet.")
            return
        else:
            print("This student has chosen these workshops:\n",sorted(l))
        cancel = str(input("Please provide the workshop number of the student you want to cancel: "))
        username = f'./student/{student_user_ID}.txt'
        d3 = (student_user_ID,int(cancel))
                
        while d3 not in l4:
            print("This student has not chosen this workshop.")
            student_user_ID = str(input("Please give the ID of the student: "))
            cancel = str(input("Please provide the workshop number of the student you want to cancel: "))
            d3 = (student_user_ID,int(cancel))
        print("Please check your choice:",end='')
        check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))

        while check != 1:
            student_user_ID = str(input("Please give the ID of the student: "))
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

        with open(workshop_csv, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            file.close()

        for line in lines:
            workshop_content = line.split(',')
            workshop_list1.append(workshop_content)

        with open(workshop_csv, 'w', encoding='utf-8', newline='') as file:
            for b in workshop_list1:
                if cancel != b[1]:
                    c = [str(int(b[0])), str(b[1]), str(b[2]),str(b[3]),str(b[4][:-1])]
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(c)
                else:
                    c = [str(int(b[0])), str(b[1]), str(b[2]),str(b[3]),str(int(b[4][:-1])+1)]
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(c)


def add_Sworkshop():

    """ This part is for the administrator to help students choose the workshop """
    
    workshop_csv = f'./admin/document/workshop.csv'
    log = f'./admin/document/log.txt'
    workshop_list1 = []
    with open(log,'r') as f:
        print("The log is:")
        data = f.readlines()[1:]
        f.close   

    s1 = ''.join(data)
    l = s1.split()
    l1 = l[::2]
    l2 = l[1::2]
    l2 = list(map(int, l2))
    if l1 == l2 == []:
        print("* No students choose workshop yet.")
    else:
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

    student_user_ID = str(input('Please give the ID of the student(Enter "Q" or "q" to select again): '))
    student_user_ID = student_user_ID.lower()
    if student_user_ID == "q":
        return
    else:
        l = []
        for i in range(len(l2)):
            d1 = {l1[i]:l2[i]}

            for key,val in d1.items():
                if key == student_user_ID:
                    l += [val]
        if l == []:
            print("This student hasn't chosen workshop yet.")
        else:
            print("This student has chosen these workshops:\n",sorted(l))    
        signup = str(input("Please give the number of the workshop which you want to add to student: "))
        username = f'./student/{student_user_ID}.txt'
        d3 = (student_user_ID,int(signup))
                
        while d3 in l4:
            print("This student has chosen this workshop.")
            student_user_ID = str(input("Please give the ID of the student: "))
            signup = str(input("Please give the number of the workshop which you want to add to student: "))
            d3 = (student_user_ID,int(signup))
        print("Please check your choice:",end='')
        check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))

        while check != 1:
            student_user_ID = str(input("Please give the ID of the student: "))
            signup = str(input("Please give the number of the workshop which you want to add to student: "))
            d3 = (student_user_ID,int(signup))

            while d3 in l4:
                print("This student has chosen this workshop.")
                student_user_ID = str(input("Please give the ID of the student: "))
                signup = str(input("Please give the number of the workshop which you want to add to student: "))
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
        
        with open(workshop_csv, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            file.close()

        for line in lines:
            workshop_content = line.split(',')
            workshop_list1.append(workshop_content)

        with open(workshop_csv, 'w', encoding='utf-8', newline='') as file:
            for b in workshop_list1:
                if signup != b[1]:
                    c = [str(int(b[0])), str(b[1]), str(b[2]),str(b[3]),str(b[4][:-1])]
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(c)
                else:
                    c = [str(int(b[0])), str(b[1]), str(b[2]),str(b[3]),str(int(b[4][:-1])-1)]
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(c)


def Authority(e):
    a = True
    if e == 1:
        storage_workshop()
        b = str(input('Enter "Q" or "q" to exit: '))
        return a
    elif e == 2:
        ws_description()
        # b = str(input('Enter "Q" or "q" to exit: '))
        return a
    elif e == 3:
        update_workshop()
        return a
    elif e == 4:
        delete_workshop()
        return a
    elif e == 5:
        retrieve_workshop()
        b = str(input('Enter "Q" or "q" to exit: '))       
        return a
    elif e == 6:
        add_Sworkshop()
        return a
    elif e == 7:
        cancel_Sworkshop()
        return a
    elif e == 8:
        retrieve_log()
        return a
    elif e == 9:
        reset_password()
        return a
    elif e == 10:
        a = False
        return a


def start():
    print("*" * 35)
    print("*" + " " * 33 + "*")
    print("*" + " " * 33 + "*")
    print("*" + " --Workshops Enrollment System-- " + "*")
    print("*" + "                    --- Group 12 " + "*")
    print("*" + " " * 33 + "*")
    print("*" + " " * 33 + "*")
    print("*" + " " * 33 + "*")
    print("*" * 35)
    print(" " * 12 + "--<START>--" + " " *12)
    enter = input(" " * 21 + "Click 'Enter'!")


def about():
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


def main():
    while True:
        a = {1:"Sign Up", 2:"Sign In", 3:"Quit", 4:"About"}
        print()
        print("-"*30)
        print("{0:^10}".format("Number"),'|',"{0:^15}".format("Function"))
        print("-"*30)
        for k,v in a.items():
            print("{0:^10}".format(k),'|',"{0:}".format(v))
        num_a = int(input('Enter the number:\n'))

        if num_a == 1:
            b = {1:"Sign Up --- Admin", 2:"Sign Up --- Students"}
            print()
            print("-"*40)
            print("{0:^10}".format("Number"),'|',"{0:^25}".format("Function"))
            print("-"*40)
            for k,v in b.items():
                print("{0:^10}".format(k),'|',"{0:}".format(v))
            num_b = int(input('Enter the number:\n'))

            Sign_Up(num_b)
        elif num_a == 2:
            c = {1:"Sign In --- Admin", 2:"Sign In --- Students"}
            print()
            print("-"*40)
            print("{0:^10}".format("Number"),'|',"{0:^25}".format("Function"))
            print("-"*40)
            for k,v in c.items():
                print("{0:^10}".format(k),'|',"{0:}".format(v))
            num_c = int(input('Enter the number:\n'))

            ID = Log_In(num_c)
            if num_c == 1:
                a = True
                while a:
                    D = {1:"Input & Storage Workshops",2:"Add Workshops Description", 3:"Update Workshops",4:"Delete Workshops",5:"Search Workshops",6:"Select Workshops for Students",7:"Cancel the Workshops select by Students",8:"Search & Read Log",9:"Reset Students' Password",10:"Log out"}
                    print()
                    print()
                    print("-"*60)
                    print("{0:^10}".format("Number"),'|',"{0:^45}".format("Function"))
                    print("-"*60)
                    for k,v in D.items():
                        print("{0:^10}".format(k),'|',"{0:}".format(v))
                    e = int(input('Enter the number:\n'))
                    a = Authority(e)

            elif num_c == 2:
                a = True
                while a:
                    d = {1:"Enroll Workshops", 2:"Cancel Workshops",3:"Read Workshops",4:"Change Password", 5:"Log out"}
                    print()
                    print("-"*35)
                    print("{0:^10}".format("Number"),'|',"{0:^20}".format("Function"))
                    print("-"*35)
                    for k,v in d.items():
                        print("{0:^10}".format(k),'|',"{0:}".format(v))
                    num_d = int(input('Enter the number:\n'))
                    a = Student(num_d,ID)

        elif num_a == 3:
            break
        elif num_a == 4:
            about()
            b = str(input('Enter "Q" or "q" to exit: '))


start()
main()
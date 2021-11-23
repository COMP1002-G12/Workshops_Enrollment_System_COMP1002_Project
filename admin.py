import csv

def judgement(workshop_list1,workshop):
    controller = True
    for i in range(len(workshop_list1)):
        if controller:
            if workshop in workshop_list1[i]:
                controller = False
    return controller

def delete_workshop():
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
        '{0:^20}'.format(field_names[3]),'{0:^20}'.format(field_names[4]),sep='')
        print('-' * 104)
        for line in lines:
            workshop_content = line.split(',')
            print('{0:^20}'.format(workshop_content[0]), '|', '{0:^20}'.format(workshop_content[1]), '|',
                '{0:^20}'.format(workshop_content[2]), '|','{0:^20}'.format(workshop_content[3]), '|','{0:^20}'.format(workshop_content[4][0:-1]), sep='')
    for line in lines:
        workshop_content = line.split(',')
        workshop_list1.append(workshop_content)
    workshop_name = str(input("Please enter the workshop name: "))
    
    while judgement(workshop_list1,workshop_name):
        print("The list does not have this workshop.")
        workshop_name = str(input("Please enter the workshop name: "))
    

    for b in workshop_list1:
        if workshop_name == b[2]:
            a = int(b[0])


    with open(workshop_csv, 'w', encoding='utf-8', newline='') as file:

        for b in workshop_list1:
            if workshop_name != b[2]:
                if int(b[0]) > a:
                    c = [str(int(b[0]) - 1), str(b[1]), str(b[2]),str(b[3]), str(b[4][:-1])]
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(c)
                else:
                    c = [str(int(b[0])), str(b[1]), str(b[2]),str(b[3]),str(b[4][:-1])]
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(c)

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

    while judgement(workshop_list1,workshop):
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
        workshop_ID = int(input("Please enter the ID of the workshop: "))
        workshop_name = str(input("Please enter the workshop name: "))

        for line in lines:
            workshop_content = line.split(',')
            workshop_list.append(workshop_content)

        for b in workshop_list:
            while workshop_name in b[2] or str(workshop_ID) in b[1]:
                print("There is already a workshop with the same ID or name, please change the ID or name: ")
                workshop_ID = int(input("Please enter the ID of the workshop: "))
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

def reset_password():
    
    """ This part can reset the student's Log_In password """
            
    student_user_ID = str(input("Please give the ID of the student: "))
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
                print("This student hasn't chosen workshop yet.")
            else:
                print("This student chose these workshops:\n",sorted(l))
        elif choose == 3:
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

    student_user_ID = str(input("Please give the ID of the student: "))
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

    student_user_ID = str(input("Please give the ID of the student: "))
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
        return a
    elif e == 2:
        delete_workshop()
        return a
    elif e == 3:
        retrieve_workshop()
        return a
    elif e == 4:
        add_Sworkshop()
        return a
    elif e == 5:
        cancel_Sworkshop()
        return a
    elif e == 6:
        retrieve_log()
        return a
    elif e == 7:
        reset_password()
        return a
    elif e == 8:
        a = False
        return a


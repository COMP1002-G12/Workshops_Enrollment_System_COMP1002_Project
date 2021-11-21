def Authority(e):
    a = True
    while a:
        if e == 1:

            """ This part is for the administrator to help students choose the workshop """

            log = f'/admin/document/log.txt'

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
            username = f'/student/{student_user_ID}.txt'
            d3 = (student_user_ID,int(signup))
            
            while d3 not in l4:
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

            log = f'/admin/document/log.txt'

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
            username = f'/student/{student_user_ID}.txt'
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

            log = f'/admin/document/log.txt'
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
            username = f'/student/{student_user_ID}.txt'
            change = int(input("Change the password: Enter 1 to reset password; Enter 2 to quit:\n"))

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
                a = False
            elif change == 2:
                a = False


        elif e == 5:
            break

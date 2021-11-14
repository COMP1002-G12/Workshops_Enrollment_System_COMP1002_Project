def Authority(e):
    if e == 1:
        student_user_ID = str(input('Please give the ID of the student:'))
        signup = str(input('Please give the number of the workshop which you want to add to student:'))
        log = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/GP/COMP1002_Group12_Project/admin/document/log.txt'                
        username = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/GP/COMP1002_Group12_Project/student/{student_user_ID}.txt'
                    
        print('Please check your choice:',end='')
        check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))
                    
        while check != 1:
            signup = str(input('Please give the number of the workshop which you want to sign up again:'))
            print('Please check your choice:',end='')
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

    elif e == 2:
        log = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/GP/COMP1002_Group12_Project/admin/document/log.txt'

        with open(log,'r') as f:
            print('The log is:')
            data = f.readlines()              
            print(''.join(data))
            f.close                                
                
        student_user_ID = str(input('Please give the ID of the student:'))
        cancel = str(input('Please provide the workshop number of the student you want to cancel:'))
                
        username = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/GP/COMP1002_Group12_Project/student/{student_user_ID}.txt'

        print('Please check your choice:',end='')
        check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))
                
        while check != 1:
            student_user_ID = str(input('Please give the name of the student:'))
            cancel = str(input('Please give the number of the workshop which you want to cancel:'))
            print('Please check your choice:',end='')
            check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))
                
        with open(username,'r') as f:
            lines = f.readlines()
                
        with open(username, "w") as f:
            for line in lines:
                if line.strip("\n") != student_user_ID+'\t'+cancel:
                    f.write(line)
                
        with open(log,'r') as f:
            lines = f.readlines()
                
        with open(log, "w") as f:
            for line in lines:
                if line.strip("\n") != student_user_ID+'\t'+cancel:
                    f.write(line)
            
            
            
            
    elif e == 3:
        log = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/GP/COMP1002_Group12_Project/admin/document/log.txt'
        l1 = []
        l2 = []
        with open(log,'r') as f:    
            print('The log is:')
            data = f.readlines()[1:]              
            f.close   
        s1 = ''.join(data)
        l = s1.split()
        l1 = l[::2]
        l2 = l[1::2]                    
        l2 = list(map(int, l2))
        print('-' * 24)
        print("{0:^12}".format("Student_ID"),'|',"{0:^12}".format("Workshops"),sep='')
        print('-' * 24)
        for i in range(len(l2)):            
            d1 = {l1[i]:l2[i]}
            for k,v in d1.items():
                print("{0:^12}".format(k),'|',"{0:^12}".format(v),sep='')

        choose = int(input("Enter 1 for inputing the workshop number to know who chose this workshop; Enter 2 for inputing student_ID to know which workshops are selected:"))
        if choose == 1:
            v = int(input("Enter the workshop number to know who chose this workshop:"))
            l = []
            for i in range(len(l2)):
                d1 = {l1[i]:l2[i]}

                for key,val in d1.items():
                    if val == v:
                        l += [key]
            print("These student_IDs chose this workshop:",l)

        elif choose == 2:
            k = str(input("Enter student_ID to know which workshops are selected:"))
            l = []
            for i in range(len(l2)):
                d1 = {l1[i]:l2[i]}

                for key,val in d1.items():
                    if key == k:
                        l += [val]    
            print("This student chose these workshops:",l)
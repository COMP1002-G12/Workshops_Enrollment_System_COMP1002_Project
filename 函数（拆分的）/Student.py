def S1(student_user_ID):
    signup = str(input('Please give the number of the workshop which you want to sign up:'))
    print('Please check your choice:',end='')
    check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))
    log = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/GP/COMP1002_Group12_Project/admin/document/log.txt'
        
    data_file = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/GP/COMP1002_Group12_Project/student/{student_user_ID}.txt'
        
     
    while check != 1:
        signup = str(input('Please give the number of the workshop which you want to sign up again:'))
        print('Please check your choice:',end='')
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

    return data_file,log                         
            
    
    

def S2(student_user_ID):

    student_user_ID = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/GP/COMP1002_Group12_Project/student/{student_user_ID}.txt'
    log = f'E:/my file/大学/香港理工大学/学习/2021-2022/COMP1002/Assessment/GP/COMP1002_Group12_Project/admin/document/log.txt'


    with open(student_user_ID,'r') as f:
        print('Your choice:')
        data = f.readlines()              
        print(''.join(data[1:]))
        f.close

    ID = str(input('Please give your ID:'))
    cancel = str(input('Please give the number of the workshop which you want to cancel:'))
    print('Please check your choice:',end='')
    check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))
                
    while check != 1:
        ID = str(input('Please give your name:'))
        cancel = str(input('Please give the number of the workshop which you want to cancel:'))
        print('Please check your choice:',end='')
        check = int(input('(Put 1 for "Yes"; Put 2 for "No")\n'))
                
    with open(student_user_ID,'r') as f:
        lines = f.readlines()
                
    with open(student_user_ID, "w") as f:
        for line in lines:
            if line.strip("\n") != ID+'\t'+cancel:
                f.write(line)
                
    with open(log,'r') as f:
        lines = f.readlines()
                
    with open(log, "w") as f:
        for line in lines:
            if line.strip("\n") != ID+'\t'+cancel:
                f.write(line)

        return student_user_ID,log

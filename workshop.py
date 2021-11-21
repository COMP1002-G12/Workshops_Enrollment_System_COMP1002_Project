import csv

def enter():
    L = []
    print("Please do not enter more than 20 letters:")
    judge = False
    while not judge:
        with open ('workshop.csv','r',encoding='utf-8') as file:
            lines = file.readlines()
            file.close()

        length = len(lines)
        workshop_ID = int(input("Please enter the ID of the workshop: "))
        workshop_name = str(input("Please enter the workshop name: "))

        for line in lines:
            contents = line.split(',')
            L.append(contents)

        for b in L:
            while workshop_name in b[2] or str(workshop_ID) in b[1]:
                print("There is already a workshop with the same ID or name, please change the ID or name: ")
                workshop_ID = int(input("Please enter the ID of the workshop: "))
                workshop_name = str(input("Please enter the workshop name: "))
        
        total = int(input("Please enter the total number of students: "))
        remind = int(input("Enter 1 for Continue, Enter 2 for Quit: "))

        if remind == 1:
            Index = length + 1
            data = [str(Index),str(workshop_ID),workshop_name,str(total)]
            with open('workshop.csv','a',encoding='utf-8',newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(data) 
            file.close()



        elif remind == 2:
            judge = True
            Index = length + 1
            data = [str(Index),str(workshop_ID),workshop_name,str(total)]
            with open('workshop.csv','a',encoding='utf-8',newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow(data) 
            file.close()




    with open ('workshop.csv','r',encoding='utf-8') as file:
        lines = file.readlines()

    field_names = ['Index','Workshop_ID','Workshop_Name','Total']




    print('-'*80)
    print('{0:^20}'.format(field_names[0]),'|','{0:^20}'.format(field_names[1]),'|','{0:^20}'.format(field_names[2]),'|','{0:^20}'.format(field_names[3]),sep='')
    print('-'*80)
    for line in lines:
        contents = line.split(',')
        print('{0:^20}'.format(contents[0]),'|','{0:^20}'.format(contents[1]),'|','{0:^20}'.format(contents[2]),'|','{0:^20}'.format(contents[3][0:-1]),sep='')



def delete():
    L1 = []
    with open ('workshop.csv','r',encoding='utf-8') as file:
        lines = file.readlines()
        file.close()
    field_names = ['Index','Workshop_ID','Workshop_Name','Total']




    print('-'*80)
    print('{0:^20}'.format(field_names[0]),'|','{0:^20}'.format(field_names[1]),'|','{0:^20}'.format(field_names[2]),'|','{0:^20}'.format(field_names[3]),sep='')
    print('-'*80)
    for line in lines:
        contents = line.split(',')
        print('{0:^20}'.format(contents[0]),'|','{0:^20}'.format(contents[1]),'|','{0:^20}'.format(contents[2]),'|','{0:^20}'.format(contents[3][0:-1]),sep='')

        
    workshop_name = str(input("Please enter the workshop name: "))

    for line in lines:
        contents = line.split(',')
        L1.append(contents)

    for b in L1:
        while workshop_name != b[2]:
            print("The list does not have this workshop.")
            workshop_name = str(input("Please enter the workshop name: "))
        if workshop_name == b[2]:
            a = int(b[0])
        

    with open('workshop.csv','w',encoding='utf-8',newline='') as file:

        for b in L1:
            if workshop_name != b[2]:
                if int(b[0]) > a:
                    c = [str(int(b[0])-1),str(b[1]),str(b[2]),str(b[3][:-1])]
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(c) 
                else:
                    c = [str(int(b[0])),str(b[1]),str(b[2]),str(b[3][:-1])]
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(c) 

    with open ('workshop.csv','r',encoding='utf-8') as file:
        lines = file.readlines()
        file.close()
    print('-'*80)
    print('{0:^20}'.format(field_names[0]),'|','{0:^20}'.format(field_names[1]),'|','{0:^20}'.format(field_names[2]),'|','{0:^20}'.format(field_names[3]),sep='')
    print('-'*80)
    for line in lines:
        contents = line.split(',')
        print('{0:^20}'.format(contents[0]),'|','{0:^20}'.format(contents[1]),'|','{0:^20}'.format(contents[2]),'|','{0:^20}'.format(contents[3][0:-1]),sep='')


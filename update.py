import csv

def judgement3(workshop_list1,workshop_ID,workshop_name):
    controller = True
    for i in range(len(workshop_list1)):
        if controller:
            if str(workshop_ID) == workshop_list1[i][1] and workshop_name == workshop_list1[i][2]:
                controller = False
    return controller

def judgement4(workshop_list1,workshop_newName):
    controller = True
    for i in range(len(workshop_list1)):
        if controller:
            if workshop_newName in workshop_list1[i]:
                controller = True
            else:
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
    
    workshop_ID = int(input('Please enter the workshop id to confirm: '))
    workshop_name = str(input("Please enter the workshop name you want to change: "))
    
    while judgement3(workshop_list1,workshop_ID,workshop_name):
        print("The entered workshop_ID does not match the workshop_name.")
        workshop_ID = int(input("Please enter the workshop id again: "))
        workshop_name = str(input("Please enter the workshop name you want to change: "))    

    with open(workshop_csv, 'w', encoding='utf-8', newline='') as file:

        n = int(input('Enter "1" if you want to change the "Workshop_Name" of the workshop. Enter "2" if you want to change the "Total" of the workshop: '))
        
        if n == 1:
            workshop_newName = str(input("Please enter a new workshop name: "))
            
            while judgement4(workshop_list1,workshop_newName):
                print("The list have this workshop.")
                workshop_newName = str(input("Please enter a new workshop name: "))

            for b in workshop_list1:
                if workshop_name == b[2] and str(workshop_ID) == b[1]:
                    c = [str(int(b[0])), str(b[1]), workshop_newName,str(b[3]),str(b[4][:-1])]     
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(c)
                else:
                    c = [str(int(b[0])), str(b[1]), str(b[2]),str(b[3]),str(b[4][:-1])]     
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(c)


        if  n ==2:
            workshop_total = int(input('Please enter a new total number of students accommodated: '))
            for b in workshop_list1:
                if workshop_name == b[2] and str(workshop_ID) == b[1]:
                    c = [str(int(b[0])), str(b[1]),str(b[2]),str(workshop_total),str(workshop_total-(int(b[3])-int(b[4][:-1])))]     
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
    '{0:^20}'.format(field_names[3]),'|','{0:^20}'.format(field_names[4]),sep='')
    print('-' * 104)
    for line in lines:
        workshop_content = line.split(',')
        print('{0:^20}'.format(workshop_content[0]), '|', '{0:^20}'.format(workshop_content[1]), '|',
              '{0:^20}'.format(workshop_content[2]), '|','{0:^20}'.format(workshop_content[3]), '|','{0:^20}'.format(workshop_content[4][0:-1]), sep='')

update_workshop()
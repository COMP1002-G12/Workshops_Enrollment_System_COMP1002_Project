import csv

workshop_list = []
workshop_content = []
print("Please do not enter more than 20 letters:")
with open ('workshop.csv','r',encoding='utf-8') as file:
    lines = file.readlines()

field_names = ['Index','Workshop_ID','Workshop_Name','Total']

print('-'*80)
print('{0:^20}'.format(field_names[0]),'|','{0:^20}'.format(field_names[1]),'|','{0:^20}'.format(field_names[2]),'|','{0:^20}'.format(field_names[3]),sep='')
print('-'*80)
for line in lines:
    workshop_content = line.split(',')
    print('{0:^20}'.format(workshop_content[0]),'|','{0:^20}'.format(workshop_content[1]),'|','{0:^20}'.format(workshop_content[2]),'|','{0:^20}'.format(workshop_content[3][0:-1]),sep='')

judge = False
while not judge:
    with open ('workshop.csv','r',encoding='utf-8') as file:
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
    workshop_content = line.split(',')
    print('{0:^20}'.format(workshop_content[0]),'|','{0:^20}'.format(workshop_content[1]),'|','{0:^20}'.format(workshop_content[2]),'|','{0:^20}'.format(workshop_content[3][0:-1]),sep='')

## Here is functions
def delete1(workshop_list1,workshop_name):
    controller = True
    for i in range(len(workshop_list1)):
        if controller:
            if workshop_name in workshop_list1[i]:
                controller = False
    return controller

def delete2():
    workshop_list1 = []
    with open('workshop.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file.close()
    field_names = ['Index', 'Workshop_ID', 'Workshop_Name', 'Total']

    print('-' * 80)
    print(
    '{0:^20}'.format(field_names[0]), '|', '{0:^20}'.format(field_names[1]), '|', '{0:^20}'.format(field_names[2]), '|',
    '{0:^20}'.format(field_names[3]), sep='')
    print('-' * 80)
    for line in lines:
        workshop_content = line.split(',')
        print('{0:^20}'.format(workshop_content[0]), '|', '{0:^20}'.format(workshop_content[1]), '|',
              '{0:^20}'.format(workshop_content[2]), '|', '{0:^20}'.format(workshop_content[3][0:-1]), sep='')
    for line in lines:
        workshop_content = line.split(',')
        workshop_list1.append(workshop_content)
    workshop_name = str(input("Please enter the workshop name: "))
    
    while delete1(workshop_list1,workshop_name):
        print("The list does not have this workshop.")
        workshop_name = str(input("Please enter the workshop name: "))
    

    for b in workshop_list1:
        if workshop_name == b[2]:
            a = int(b[0])


    with open('workshop.csv', 'w', encoding='utf-8', newline='') as file:

        for b in workshop_list1:
            if workshop_name != b[2]:
                if int(b[0]) > a:
                    c = [str(int(b[0]) - 1), str(b[1]), str(b[2]), str(b[3][:-1])]
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(c)
                else:
                    c = [str(int(b[0])), str(b[1]), str(b[2]), str(b[3][:-1])]
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(c)

    with open('workshop.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file.close()
    print('-' * 80)
    print(
    '{0:^20}'.format(field_names[0]), '|', '{0:^20}'.format(field_names[1]), '|', '{0:^20}'.format(field_names[2]), '|',
    '{0:^20}'.format(field_names[3]), sep='')
    print('-' * 80)
    for line in lines:
        workshop_content = line.split(',')
        print('{0:^20}'.format(workshop_content[0]), '|', '{0:^20}'.format(workshop_content[1]), '|',
              '{0:^20}'.format(workshop_content[2]), '|', '{0:^20}'.format(workshop_content[3][0:-1]), sep='')



def retrieval():
    workshop_list1 = []
    with open('workshop.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()
        file.close()
    field_names = ['Index', 'Workshop_ID', 'Workshop_Name', 'Total']

    print('-' * 80)
    print(
    '{0:^20}'.format(field_names[0]), '|', '{0:^20}'.format(field_names[1]), '|', '{0:^20}'.format(field_names[2]), '|',
    '{0:^20}'.format(field_names[3]), sep='')
    print('-' * 80)
    for line in lines:
        workshop_content = line.split(',')
        print('{0:^20}'.format(workshop_content[0]), '|', '{0:^20}'.format(workshop_content[1]), '|',
              '{0:^20}'.format(workshop_content[2]), '|', '{0:^20}'.format(workshop_content[3][0:-1]), sep='')

    workshop_name = str(input("Please enter the workshop name: "))

    for line in lines:
        workshop_content = line.split(',')
        workshop_list1.append(workshop_content)

    for b in workshop_list1:
        while workshop_name != b[2]:
            print("The list does not have this workshop.")
            workshop_name = str(input("Please enter the workshop name: "))
        if workshop_name == b[2]:
            a = int(b[0])
            b = int(b[1])
            c = b[2]
            d = b[3]

    find_name = [a, b, c, d]

    print('-' * 80)
    print(
    '{0:^20}'.format(find_name[0]), '|', '{0:^20}'.format(find_name[1]), '|', '{0:^20}'.format(find_name[2]), '|',
    '{0:^20}'.format(find_name[3]), sep='')
    print('-' * 80)
    for line in lines:
        workshop_content = line.split(',')
        print('{0:^20}'.format(workshop_content[0]), '|', '{0:^20}'.format(workshop_content[1]), '|',
              '{0:^20}'.format(workshop_content[2]), '|', '{0:^20}'.format(workshop_content[3][0:-1]), sep='')
## Here is the action to call the functions
while True:
    n = input('please enter the action(delete/update/retrieval/quit):')

    if n == 'delete':
        delete2()
    elif n == 'update':
        print("Please do not exceed 20 letters for the total workshops:")
        judge = False
        while not judge:
            with open('workshop.csv', 'r', encoding='utf-8') as file:
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

            total = int(input("Please enter the total number of students: "))
            remind = int(input("Enter 1 for Continue, Enter 2 for Quit: "))

            if remind == 1:
                Index = length + 1
                data = [str(Index), str(workshop_ID), workshop_name, str(total)]
                with open('workshop.csv', 'a', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(data)
                file.close()

            elif remind == 2:
                judge = True
                Index = length + 1
                data = [str(Index), str(workshop_ID), workshop_name, str(total)]
                with open('workshop.csv', 'a', encoding='utf-8', newline='') as file:
                    csv_writer = csv.writer(file)
                    csv_writer.writerow(data)
                file.close()

            with open('workshop.csv', 'r', encoding='utf-8') as file:
                lines = file.readlines()

            field_names = ['Index', 'Workshop_ID', 'Workshop_Name', 'Total']

            print('-' * 80)
            print('{0:^20}'.format(field_names[0]), '|', '{0:^20}'.format(field_names[1]), '|',
                  '{0:^20}'.format(field_names[2]), '|', '{0:^20}'.format(field_names[3]), sep='')
            print('-' * 80)
            for line in lines:
                workshop_content = line.split(',')
                print('{0:^20}'.format(workshop_content[0]), '|', '{0:^20}'.format(workshop_content[1]), '|',
                      '{0:^20}'.format(workshop_content[2]), '|', '{0:^20}'.format(workshop_content[3][0:-1]), sep='')
    elif n == 'retrieval':
        retrieval()

    elif n == 'quit':
        break
    else:
        n = input('Please enter a correct order')





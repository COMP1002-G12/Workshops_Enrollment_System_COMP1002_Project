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


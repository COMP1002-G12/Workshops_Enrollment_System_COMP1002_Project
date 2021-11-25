def description():

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
        if int(workshop_content[1]) == i_ID:
            desc = input(workshop_content[2] + "--- Description: ")
            desc_file = f'./admin/document/workshop/{workshop_content[2]}.txt'
            with open(desc_file, 'w') as f:
                    f.write(desc)

description()
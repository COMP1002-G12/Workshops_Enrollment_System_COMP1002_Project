
a = int(input("Sign In: Enter 1 for Admin; Enter 2 for Student\n"))

if a == 1:
    admin_user = str(input("Admin Username: "))
    admin_passwd = str(input("Enter Admin Password: "))

    data_file = f'C:/Users/David/Desktop/COMP1002/Group12_Project/{admin_user}.txt'

    with open(data_file) as f:
        contents = f.readlines()
        #data_contents = contents.split()
    print(contents)

    if contents[0] == admin_passwd:
        print("Successful into Workshop Enroll System ---Admin Account")

    else:
        print("Error to Login: Wrong Password or User Name")


if a == 2:
    student_user = str(input("Student Username: "))
    student_passwd = str(input("Enter Student Password: "))

    data_file = f'C:/Users/David/Desktop/COMP1002/Group12_Project/{student_user}.txt'

    with open(data_file) as f:
        contents = f.readlines()
    print(contents)

    if contents[0] == student_passwd:
        print("Successful into Workshop Enroll System ---Student Account", student_user)
        
        print("1. ")
        select_workshop = input("Please input the Workshop you want to join: ")






    else:
        print("Error to Login: Wrong Password or User Name")
            
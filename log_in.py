import os

def Log_In(c):
    
    """ This part is to log in to the workshop system """
    
    if c == 1:
        judge = False
        while not judge:
            
            admin_user = str(input("Admin Username: "))
            admin_passwd = str(input("Enter Admin Password: "))            
            data_file = f'./admin/user/{admin_user}.txt'
            pathDir = os.listdir('./admin/user')
            T = admin_user + '.txt'
            
            if T not in pathDir:
                print("Error! This Admin Account has not been registered yet, please enter correct account.")
            else:
                judge = True
                with open(data_file) as f:
                    contents = f.readline().splitlines()
                    line1 = contents[0]

                while line1 != admin_passwd:
                    print("Error to Login: Wrong Password.")
                    admin_passwd = str(input("Enter Student Password: "))
                
                if line1 == admin_passwd:
                    print("Successful into Workshop Enroll System --- Admin Account")
            
                return 1

    if c == 2:
        judge = False
        while not judge:
            
            student_user_ID = str(input("Student ID: "))
            student_passwd = str(input("Enter Student Password: "))
            data_file = f'./student/{student_user_ID}.txt'
            pathDir = os.listdir('./student')
            T = student_user_ID + '.txt'
            
            if T not in pathDir:
                print("Error! This Student Account has not been registered yet, please enter correct account.")
            else:
                judge = True
                with open(data_file) as f:
                    contents = f.readline().splitlines()
                    line1 = contents[0]
                    
                while line1 != student_passwd:
                    print("Error to Login: Wrong Password.")
                    student_passwd = str(input("Enter Student Password: "))

                if line1 == student_passwd:
                    print("Successful into Workshop Enroll System --- Student Account", student_user_ID)
                
                return 2

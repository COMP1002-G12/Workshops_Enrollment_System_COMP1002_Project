from sign_up import Sign_Up
from log_in import Log_In
from admin import Authority
from student import S1
from student import S2
from student import S3
#from workshop import 

import os
import csv

print("*" * 35)
print("*" + " " * 33 + "*")
print("*" + " " * 33 + "*")
print("*" + " --Workshops Enrollment System-- " + "*")
print("*" + "                    --- Group 12 " + "*")
print("*" + " " * 33 + "*")
print("*" + " " * 33 + "*")
print("*" + " " * 33 + "*")
print("*" * 35)


while True:
    a = int(input('Enter 1 for sign up; Enter 2 for sign in; Enter 3 for quit; Enter 4 for About:\n'))
    if a == 1:
        b = int(input("Sign Up: Enter 1 for Admin; Enter 2 for Student\n"))
        Sign_Up(b)
    elif a == 2:
        c = int(input("Sign In: Enter 1 for Admin; Enter 2 for Student\n"))
        ID = Log_In(c)
        if c == 1:
            D = {1:"Add workshop for student",2:"Cancel workshop for student",3:"Read the workshop",4:"Reset the student's Log_In password"}
            print("{0:^10}".format("Number"),'|',"{0:^50}".format("Function"))
            print("-"*60)
            for k,v in D.items():
                print("{0:^10}".format(k),'|',"{0:}".format(v))
            e = int(input('Enter the number:\n'))
            Authority(e)
        if c == 2:
            d = int(input('Enter 1 for sign up workshop; Enter 2 for cancel workshop; Enter 3 for change password:\n'))
            while True:
                if d == 1:
                    S1(ID)
                elif d == 2:
                    S2(ID)
                elif d == 3:
                    S3(ID)
                elif d == 4:
                    break
    elif a == 3:
        break
    elif a == 4:
        print("*" * 41)
        print("*" + " " * 15 + "--About--" + " " * 15 + "*")
        print("*" + " " * 39 + "*")
        print("*" + " Name: Workshops Enrollment System     " + "*")
        print("*" + " Production team: COMP1002 Group 12    " + "*")
        print("*" + " " * 39 + "*")
        print("*" + " Members:" + " " * 30 + "*")
        print("*" + " JIANG Guanlin (21093962d)" + " " * 13 + "*")
        print("*" + " LIU Minghao (21096308d)" + " " * 15 + "*")
        print("*" + " CHEN Ziyang (21095751d)" + " " * 15 + "*")
        print("*" + " HE Boyan (21096184d)" + " " * 18 + "*")
        print("*" + " " * 39 + "*")
        print("*" + "Software Copyright© belongs to Group 12" + "*")
        print("*" + " " * 39 + "*")
        print("*" * 41)
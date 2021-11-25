def student_check_ws():
    workshop_id = input("Enter the Workshop ID: ")
    desc_file = workshop_id + ".txt"
    file_dir = "./admin/document/workshop/"
    file = file_dir + desc_file
    
    with open(file, "r") as f:
        content = f.readlines()
    print()
    print("Description: " + ''.join(content))

student_check_ws()
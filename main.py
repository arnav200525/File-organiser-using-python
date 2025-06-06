#prerequisites to run this program 
'''
1. Create a folder in your system
2. Copy this python file to that xyz folder
3. Run
'''

import os

def create_file(filename):
    try: 
        with open(filename, "x") as f:    #x use hota hai new file create karneke liye (just a file without any extension)
            print("File ",filename, "successfully created")
    except Exception as e:
        print("Error occured", e)

# fname=input("Enter file name to be created ")
# create_file(fname)

def view_file_name():
    files = os.listdir()  #return list of all files in the directory (optional-arguement as a path le sakta) if giving path '/' must be used
    if not files:
        print("Directory in empty")
    else:
        for file in files:   #.listdir() list type return karta hai that's why for loop 
            print(file)

def delete_file(filename):
    try:
        os.remove(filename)  #removes file (note: only removes file not directory)
        print(filename,"deleted")
    except:
        print("File not found")

def read_file(filename):
    try:
        with open(filename, "r") as f:  #r open files in read mode
            print(f.read())
    except:
        print("An error occured")

def edit_file(filename):
    choice = int(input(("For overwriting select 1\n For Appending select 2 ")))
    try:
        if choice == 1:
            try:
                with open(filename, "w") as f:  #w overwrites content in the file
                    content = input("Enter content to be overwitten ")
                    f.write(content)
                    print("Content overwritten successfully")
            except:
                print("An error occured")
        elif choice == 2:
            try:
                with open(filename, "a") as f:  #a appends content i.e add content at the end of file
                    content = input("Enter content to be appended ")
                    f.write("\n",content)
                    print("Content appended successfully")
            except:
                print("An error occured")
    except:
        print("Please click a valid input (1 or 2)")
    

#Main code where functions will be called

print("File Manager Using Python")
print("Operation Can be performed")
while True:
    print("1. Create file\n2. Edit File\n3. Read File\n4. List all files\n 5. Delete file\n6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        fname = input("Enter file name to be created: ")
        create_file(fname)
    elif choice == 2:
        fname = input("Enter file name to be edited: ")
        edit_file(fname)
    elif choice == 3:
        fname = input("Enter file name to be printed: ")
        read_file(fname)
    elif choice == 4:
        view_file_name()
    elif choice ==5:
        fname = input("Enter file name to be deleted: ")
        delete_file(fname)
    elif choice == 6:
        break
    else:
        print("Please enter valid choice (1-5) based on operation")

print("Operations successfully Completed!")


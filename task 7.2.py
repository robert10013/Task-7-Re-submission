#Write a another python function to read from a text file. 
#The function will take the name of the text file and display the content of the file into the console.

import os

def file_reader():
    #get file name from user
    file_name = input("Enter the file name : ")
    #check proper file name has entered
    if ".txt" not in file_name.lower():
        file_name = file_name + ".txt"

    #check if file is exists then print the results
    if os.path.isfile(file_name):
        with open(file_name,'r') as file:
            content = file.read()
            if content == "":
                print("The text file is empty...")
            else:
                print(content)
    else:
        print("file name doesn't exist")
    

#main code
#call the function
file_reader()
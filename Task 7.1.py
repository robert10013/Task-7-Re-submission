"""Write a python program using function to which will do following:-
    a)The function will create a text file with the current timestamp.
    b)The file content should have the content of the current timestamp"""
import time

#function for file handling
def txt_file_create(file_name):

    open(file_name, 'a')
    with open(file_name, 'w') as file:
        content = str(time.time())
        file.write(content)
    return 0


#Main code
current_time_stamp = time.time()
f_name = str(current_time_stamp) + ".txt"
txt_file_create(f_name)
print("where there is a will there is a way")
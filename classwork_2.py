import os

#Create a new directory.

new_directory='New_directory'
os.mkdir(new_directory)

# List all files and directories in the current working directory.

# for item in os.listdir():
#     print(item)

#Create a new text file within the newly created directory and write some content to it.

file_path=os.path.join(new_directory,'classwork2.txt')

with open(file_path,'w') as f_write:
    f_write.write("Hello this is a sample text file for classwork 2.\nThis file is written by the help of os module in python.")

#Read the content of the newly created text file.

with open(file_path,'r') as f_read:
    content=f_read.read()
    print(content)

#Rename the text file.

new_file_path=os.path.join(new_directory,'rename_classwork2.txt')
os.rename(file_path,new_file_path)

#List all files and directories in the new directory after renaming the file.

# for item in os.listdir():
#     print(item)

#Delete the new directory and its contents. 

os.remove(new_file_path)
os.rmdir(new_directory) 

for item in os.listdir():
    print(item)

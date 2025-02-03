import os
import shutil
# Step 1:::create a file and write the content in the file 
file_name="code.txt"
with open(file_name,"w") as file :
 file.write("File handling coding inside the code txt file .edited file")
print(f" File '{file_name}'")

#Step 2:: open the file in read mode

with open(file_name,"r") as file :
    content =file.read()
    print(content)

#step 3:: Rename the file 
#rename_file="Python_coding.txt"
#os.rename(file_name,rename_file)
#print(f"rename the file from code.txt file to rename_file '{rename_file}'")

#Step 4:: Move the file to directory  

create_directory="Directory_folder"
os.makedirs(create_directory, exist_ok=True)
directory_path=os.path.join(create_directory,file_name)
shutil.move(file_name,directory_path)
print(f"move the file to Directory'{directory_path}'")


#remove the file 
os.remove(directory_path)
print(f"remove file from the directory folder'{directory_path}'")

#remove directory folder if it is empty
os.rmdir(create_directory)
print(f"remove the directory '{create_directory}'")

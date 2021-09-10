# Auhor -> Rudra Rathi

# Importing libraries
import os
import time

# creating variables
path  = input("Enter the path\n")
days = int(input("Till how many days do you want to remove files\n"))
days = time.time() - days * 24 * 60 * 60 

# checking paths
path_exists = os.path.exists(path)
ctime = os.stat(path).st_ctime

#doing what to do if path is true 
if(path_exists):
    list = os.walk(path)
    for subfolder,folders,files in list:

        if days > ctime:
            os.remove(folders)
            os.remove(files)
            os.remove(subfolder)
        


else: # telling what to do if path is false
    print("Error path not found")
    time.sleep(4)
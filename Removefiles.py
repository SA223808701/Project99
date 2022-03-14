
import shutil
import os
import time

path = input("Enter the name of the file to be deleted")
path = '/usr/local/bin'

isExist = os.path.exists(path)

True

time.time()


list_of_files = os.listdir(path)

for file in list_of_files:
    name, ext = os.path.splitext(file)

    ext  = ext[1:]

    if ext== '':
        continue



    if os.path.exists(path+'/'+ext):
        shutil.move(path+ '/'+ file, path+'/'+ext+ '/'+file)




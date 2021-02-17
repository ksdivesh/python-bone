import os
from datetime import datetime

# to change the current directory
os.chdir('C:\\Users\\DIVESH\\PycharmProjects\\FirstApp\\module-os')

# to get a current directory we are working in
print(os.getcwd())

# to get a files and folder of the current directory
print(os.listdir())

#for creating directory
os.mkdir('OS-demo')

#for creating intermediate levels in the directory
os.makedirs('OSS-demo/level-1')

#for removing the directory
os.rmdir('OS-demo')

#for removing the directory with intermediate levels
os.removedirs('OSS-demo/level-1')

#renaming file or folder, first arg orginal file name
os.rename('test.txt', 'demo.txt')

#to get the information about the file
os.stat('demo.txt')

mod_time = os.stat('demo.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

#walk through the directory

for dirpath, dirnames, filenames in os.walk('C:\\Users\\DIVESH\\PycharmProjects\\FirstApp\\module-os'):
    print('Current Path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files ', filenames)
    print()



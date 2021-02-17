import os
from datetime import datetime
#
# print(os.getcwd())
#
# print(os.listdir())

# os.mkdir('demo-os')

# os.makedirs('demo-oss/folder1/subfolder1')

# os.rmdir('demo-os')

# os.removedirs('demo-oss/folder1/subfolder1')

# statFile = os.stat('test.txt')
# mtime = statFile.st_mtime

# print(datetime.fromtimestamp(mtime))

# print(os.getcwd())



# for dirpath, dirnames, filenames in os.walk('C:\\Users\\DIVESH\\PycharmProjects\\FirstApp'):
#     print(dirpath)
#     print(dirnames)
#     print(filenames)
#     print()


# path = os.getcwd()
# path = path + '\\' + 'module-oss'
#
# if(os.path.isdir(path)):
#     pass
# else:
#     os.mkdir(path)

path = os.getcwd()
path = path + '\\' + 'test.txt'
print(os.path.isfile(path))
import os

print(os.environ)
print(os.environ.get('ALLUSERSPROFILE'))

file_path = os.path.join(os.environ.get('APPDATA'), 'test.txt')
print(file_path)

#to check, is the path exists
print(os.path.exists(file_path))

#to it is a directory
print(os.path.isdir(file_path))

#to check, is it a file
print(os.path.isfile(file_path))

#to split file root and extension
print(os.path.splitext(file_path))


#to get os path
print(dir(os.path))
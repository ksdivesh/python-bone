# f = open('test.txt', 'r')
#
# print(f.mode)
#
# f.close()

with open('test.txt', 'r') as f:

    # read content from file
    f_contents = f.read()

    #you can specify the length of characters that you want to read
    # f_contents = f.read(5)

    #It allows to read again file from the start
    # f.seek()

    #read first line from the file
    # f_contents = f.readline()

    #read all lines from the file
    # f_contents = f.readlines()

    # print(f_contents)

    #tell the total number of characters in the file
    # print(f.tell())




# check file is closed
# print(f.closed)
# file = open('test2.txt', 'r')
#
# file_content = file.read()
# print(file_content)
#
# file.close()

with open('test2.txt', 'r') as file:
    file_content = file.read()

    #print total number of characters in file
    print(file.tell())

    # to show the mode
    # print(file.mode)

    # print first line
    # file_content = file.readline()

    #print all lines
    # file_content = file.readlines()


    # print(file_content)
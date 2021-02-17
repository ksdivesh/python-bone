#way to copy the file

with open('test2.txt', 'r') as file1:
    with open('test5.txt', 'w') as file2:
        for line in file1:
            print(line)
            file2.write(line)


# with open('test.txt', 'r') as rf:
#     with open('test2.txt', 'w') as wf:
#         for line in rf:  #for each line in our file
#             wf.write(line) #write the line to 2nd file
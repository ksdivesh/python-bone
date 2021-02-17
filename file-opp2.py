with open('test4.txt', 'w') as file:
    file.write('Name')
    file.write('Divesh')

    file.seek(0)

    file.write('Kumar')
    file.write('Sharma')


# way to copy file
with open('test2.txt', 'r') as file1:
    with open('test5.txt', 'w') as file2:
        for line in file1:
            print(line)
            file2.write(line)


#way to copy picture file

with open('photo-test.jpg', 'rb') as rf:
    with open('test9.png', 'wb') as wf:
        for line in rf:  #for each line in our file
            wf.write(line) #write the line to 2nd file


#copy with chunk

with open('test-pic.png', 'rb') as rf:
    with open('test-pic-copy3.png', 'wb') as wf:
        chunk_size = 100
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)


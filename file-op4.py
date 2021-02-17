#way to copy picture file

with open('photo-test.jpg', 'rb') as rf:
    with open('test9.png', 'wb') as wf:
        for line in rf:  #for each line in our file
            wf.write(line) #write the line to 2nd file

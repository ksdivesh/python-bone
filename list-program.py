#python list
# a = [1, 2.5, 'chaaadsf', 5.2]
# a[2] = 8
# print(a)





# print(type(a))

# print(a[2])

# print(len(a))

# print(a)



#python tuples
tupleList = (1, 2, '34234', 43242)
# print(tupleList[2])


#python dictionary
#It works on key=>value pair


studentOne = {
    'name': 'Rajan',
    'rollNumber': 'CSE-2012',
    'age' : 25,
    'fee' : 500.00
}


studentTwo = {
    'name': 'Tejendra',
    'rollNumber': 'CSE-2045',
    'age' : 25,
    'fee' : 600.00
}


studentList = [studentOne, studentTwo]

studentList[1]['age'] = 50

print(studentList)

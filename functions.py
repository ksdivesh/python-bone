# def hello_func():
#     pass

'''

def hello_func():
    print("hello function")


'''


# def hello_func():
#     return 'Hello function'
#
# print(hello_func())


# def hello_func(greeting, name):
#     return '{}, {}'.format(greeting, name)
#
#
# result = hello_func('hello', 'world')
#
# print(result)



def student_info(*args, **kwargs):
    print(args)
    print(kwargs)


# student_info('Math', 'Science', 'Hindi', 'English', name='Divesh', rollNumber=10)

subjects = ('Math', 'Science', 'Hindi', 'English')
stundentInformation = {'name': 'Divesh', 'rollNumber': 10}

student_info(*subjects, **stundentInformation)


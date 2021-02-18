try:
    f = open('test.txt')

    if f.name == 'test.txt':
        raise Exception('This file is not allowed')

    # var = bad_var
except FileNotFoundError:
    print('filenot found')
except Exception as e:
    print(e)
    # print('Something went wrong, message = ', e)
else:
    print('Else part')
finally:
    # f.close()
    print('Always run')







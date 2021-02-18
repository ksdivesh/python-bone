try:
    f = open('test.txt')
    if f.name == 'test.txt':
        raise Exception('This is corrupt file') #this is a way to throw an exception
    else:
        print('ok')

except FileNotFoundError as e:
    print('file does not exists ', e)
except Exception as e:
    print('something went wrong ', e)
else:  #else block only runs if we don't have any exception whether, final block always runs.
    print(f.read())
    f.close()
finally:
    print('always runs')



#comparisions

#Equal ==
#Not Equal ==


#boolean comparisions
#and
#not
#or


#False values

#False
#None
#Zero of any numeric
#Any empty sequence '', {}, []
#Any empty mapping {}


language = 'Java'

if language == "Python":
    print("Hello World")
elif language == "Java":
    print("Java")
elif language == 'Javascript':
    print("Javascript")
else:
    print("no match")


logged_in = True

if language == 'Java' and logged_in:
    print("Logged in")
else:
    print("Bad credentials")

if not logged_in:
    print("Please login ")
else:
    print("You are logged in")


a = 10
b = 10

if a is b:
    print("a==b")
else:
    print("a!=b")

print(id(a))
print(id(b))



list1 = [1, 2, 3]
list2 = [1, 2, 3]

if list1 is list2:
    print("list equal")
else:
    print("list not equal")

print("List ids")

print(id(list1))
print(id(list2))



#python object oriented programming

#A class is blueprint for creating instances. We have multiple instances of a class.
#Class contains members and methods.
#Instance variable contain data that has unique instance.


class Employee:

    #constructor
    def __init__(self, first, last, email, pay): #self recieves the instance at the first argument automatically
        self.first = first
        self.last = last
        self.pay = pay
        self.email = email

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


# emp1 = Employee()
# emp2 = Employee()
# the way below is the manual assignment
# emp1.first = 'John'
# emp1.last = 'Doe'
# emp1.email = 'johndoe@mail.com'
# emp1.pay = 1000
#
# emp2.first = 'Naman'
# emp2.last = 'Kumar'
# emp2.email = 'naman@gmail.com'
# emp2.pay = 2000



# print(emp1.first)
# print(emp2.last)

#when we create the instance then, init method will be called automatically, emp1 will passed in as self and then it will set all of these attributes
emp1 = Employee('Divesh', 'Kumar', 'diveshkrsharma@gmail.com', 1000)
# print(emp1.fullname())

print(Employee.fullname(emp1))

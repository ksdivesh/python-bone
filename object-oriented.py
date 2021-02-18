class Employee:

    #constructor
    def __init__(self, firstName, lastName, email, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.salary = salary




    def setEmployee(self, firstName, lastName, email, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.salary = salary

    def showEmployee(self):
        print('FirstName: {}, Last Name: {}, Email: {}, Salary: {}'.format(self.firstName, self.lastName, self.email, self.salary))

    def setName(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName


# emp1 = Employee()
# emp2 = Employee()

#manual assignment
# emp1.firstName = 'John'
# emp1.lastName = 'Doe'
# emp1.email = 'johndoe@company.com'
# emp1.salary = 10000


# print(emp1.firstName)
# print(emp2)

# emp1 = Employee(firstName='John', lastName='Doe', email='diveshkrsharma@gmail.com', salary=10000)

emp1 = Employee()
emp1.setEmployee(firstName='John', lastName='Doe', email='diveshkrsharma@gmail.com', salary=25000)
# emp1.setName(firstName='Divesh', lastName='Kumar')
emp1.showEmployee()

# Employee.showEmployee(emp1)

# emp1.firstName = 'John'
# emp1.lastName = 'Doe'
# print(emp1.firstName)
# print(emp1.lastName)



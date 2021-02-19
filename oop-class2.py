#Class variables | Instance variables
#Class methods | Static Methods | Instance methods

class Employee:

    raise_amount = 1.05

    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary


    def raise_salary(self):
        self.salary = self.salary * self.raise_amount

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, salary = emp_str.split('-')
        return cls(first, last, salary)

    @staticmethod
    def test_static_method():
        return "Test string"


# emp1 = Employee('Divesh', 'Kumar', 1000)
# emp2 = Employee('Naman', 'Sharma', 2000)

# emp1.raise_salary()
# emp1.raise_amount = 2
# print(emp1.__dict__)

# print(emp1.raise_amount)
# Employee.raise_amount = 2
# print(Employee.raise_amount)


# print(emp1.raise_amount)

# print(emp1.salary)


# Employee.set_raise_amount(2)
# print(Employee.raise_amount)
#
# print(emp1.raise_amount)


emp_str_1 = 'John-Doe-7000'
emp_str_2 = 'Steve-Smith-3000'

new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.test_static_method())

# print(new_emp_1.firstName)


print(Employee.test_static_method())

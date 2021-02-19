class Student:

    #class variables
    pie = 3.14
    school = "PBPS"
    subject = "English"

    def __init__(self, firstName, lastName, rollNumber, fee):

        #instance variables
        self.firstName = firstName
        self.lastName = lastName
        self.rollNumber = rollNumber
        self.fee = fee

    #instance methods
    def showInfo(self):
        return 'Name: {} {}, Roll Number: {}, Fee: {}'.format(self.firstName, self.lastName, self.rollNumber, self.fee)


    @classmethod
    def testClassMethod(cls):
        print("Class method running {} {}".format(cls.subject, cls.school))

    @staticmethod
    def getCurrentDate():
        print("Static method running")




student1 = Student('John', 'Doe', 23, 1000)
student2 = Student('Naman', "Kr", 36, 2000)

student1.subject = "Science"
Student.subject = "Maths"

# print(student1.subject)
# print(Student.subject)
# print(student2.subject)

# print(student1.__dict__)
# print(Student.__dict__)
# print(student1.subject)


# print(Student.subject)

# print(Student.subject)
# print(student1.subject)

# print(student1.school)
# student1.testvairable = "eaasdfasdf"

# print(student1.__dict__)

# print(student1.showInfo())


#class methods
Student.school = "ABC"

# Student.testClassMethod()
# student1.testClassMethod()


Student.testStaticMethod()

# instance variable | class variable
# instance methods | class methods | static methods

class Student:
    def __innit__(self):
        self.student_name = input ("\n Enter the student name: ")
        self.student_age = input ("Enter the student age: ")
        self.student_gender = input("Enter the student gender: ")

    def display(self) :
        print("Enter the student name: ",self.student_name)
        print("Enter the student age: ",self.student_age)
        print("Enter the student gender: ",self.student_gender)

class Marks:
    def __innit__(self) :
        self.grade = input ("enter the grade of the student: ")
        print("-----Evalute Marks per subject -------")
        self.english = input("Mark in English subject: ")
        self.maths = input("Mark in maths subject: ")
        self.physics = input("Mark in physics subject: ")
        self.chemistry = input("Mark in chemistry subject: ")
        self.ict = input("Mark in ict subject: ")
    def result(self) :
        self.total = self.english + self.maths + self.physics + self.chemistry + self.ict
        print("Total Evaluated Marks: ",self.total)

class Data(Student,Marks) :
    def __innit__(self):
      Student.__innit__(self)
      Marks.__innit__(self)

    def result(self):
        Marks.display(self)
s1 = Data()
s1.result
s2 = Data()
s2.result
print("you can creat more objects")

class Student:
    a="Student"#class variable
    def __init__(self,name,age,phone_no):
        print(self)
        self.name=name#instance variable
        self.age=age
        self.phone_no=phone_no

    def booting(self):
        print("Booting....")
Manoj=Student(18,1345678908)
Arun=Student(18,1024859086)
Varun=Student(18,6768906746)
print("Arun=",Arun)            

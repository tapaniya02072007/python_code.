class Student: 
#this i a special method called constructor 
    def __init__(self): 
        self.name="jns" 
        self.age=20 
        self.marks=88 
#this is an instance method 
    def talk(self):
        print("Hi")
        print("i am ",self.name) 
        print("My age is:- ",self.age) 
        print("My marks are:- ",self.marks) 
#create an instance to Student class 
s1=Student() 
#call the method using the instance 
s1.talk() 

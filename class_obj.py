class Student:   
    def __init__(self):
        self.name="jenish"
        self.age=20
        self.marks=68 
    def talk(self):
        print("hi")
        print("i am",self.name) 
        print("my age is:-",self.age) 
        print("my marks are:-",self.marks)
s=Student()
s.talk()

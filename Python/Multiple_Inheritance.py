class Teacher:
    def __init__(self):
        pass

    def teach(self):
        print('I am teaching')

class Student:
    def __init__(self):
        pass

    def go_class(self):
        print('I am going to class to learn and study')

class Youtuber:
    def __init__(self):
        pass

    def stream(self):
        print('I am on a live stream video on Youtube')

class Me(Teacher,Student,Youtuber):
    def __init__(self):
        super().__init__()


teslim = Me()
teslim.stream()
teslim.teach()
teslim.go_class()
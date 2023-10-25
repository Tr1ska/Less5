class Human:
    height = 180

class Student(Human):
    gladness=0

class Worker(Human):
    gladness=30

kira = Student()
evgen = Worker()
print(kira.gladness)
print(evgen.gladness)
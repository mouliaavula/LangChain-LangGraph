class Employee:
    pass
class Customer:
    pass
class Student:
    pass
l = [Employee(),Customer(),Student()]
for obj in l:
    #print(obj)
    print(type(obj).__name__)
    
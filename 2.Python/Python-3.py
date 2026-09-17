class Employee:
    pass
class Customer:
    pass
class Student:
    pass
l = [Employee(),Customer(),Student()]
for obj in l:
    print(obj)
    print(type(obj))
    print(type(obj).__name__)

# pass is a null statement used as a placeholder when a block of code cannot be empty.
# It is a placeholder used when Python requires a statement, but you don't want to write any code there yet.
'''
def my_function():
    pass
Here, Python expects something inside the function. If you leave it empty:
    
def my_function():
    
you get an error.
'''

'''
type(x) → gives the class/type object
type(x).__name__ → gives the class name as a string
Ex:
type(x)           → <class 'int'>
type(x).__name__  → "int"

'''

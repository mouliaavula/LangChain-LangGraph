x = int(input("Enter First Number: "))
y = int(input("Enter Second number"))
#print(x/y)

# o/p:
"""
Enter First Number: 10
Enter Second Number: 0
Traceback ...
...
ZeroDivisionError: division by zero
"""
#========================================================================================
"""
try:
    print(x/y)
except:
    print("Error raised")
"""
# o/p:    
"""
Enter First Number: 10
Enter Second number0
Error raised
"""
# ======================================================================================

try:
    print(x/y)
except ZeroDivisionError as e:
    print("Error raised: ",e)
    
#o/p:

""" 
Enter First Number: 10
Enter Second number0
Error raised:  division by zero
"""
    

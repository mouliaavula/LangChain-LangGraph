x = int(input("Enter First Number:"))
y = int(input("Enter Second number:"))
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
# catches any exception and continuous with normal flow. no abnormal termination
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
# catches only ZeroDivisionError and normal flow continued . if any other exception again it is abnormal termination
#o/p:

""" 
Enter First Number: 10
Enter Second number0
Error raised:  division by zero
"""
    

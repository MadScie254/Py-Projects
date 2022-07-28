#nested if else statement
from ctypes.wintypes import PLARGE_INTEGER
from msilib.schema import Condition
import this


#if Condition:
#    if another Condition:
#        do this
#    else:
#       do this
#else:
#        do this

print("Welcome to roller coaster Ride!!!")

height = int(input("Please enter height\n"))

if height >= 120:
    print("Welcome to the roller coaster Ride!!")
    
    age = int(input("Please enter age"))
    
    if age > 18:
        print("Please pay 7$")
    
    else:
        print("Please pay 12$")
else:
    print("Sorry you are not allowed")




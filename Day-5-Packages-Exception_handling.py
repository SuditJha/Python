# Built in package --> install from pip

# Exception

# try :
#     print(x)
# except:
#     print("Unexpected Error")
# else:
#     print("No Error")

# try:
#     print("hello")
# except:
#     print("Error")
# else:
#     print("Nothing went wromg")


# try:
#     print(x)
# except:
#     print("x not Defined")
# finally:
#     print("Closes Try Except case")

# # User defined error
# # for no negative number available

# x=-1
# if x<0:
#     raise Exception("No negative number allowed")

a = int(input("Enter a number : "))
b = int(input("Enter a number : "))

try:
    print(a/b)
except:
    print("Cannot divide by 0")
else:
    print("Division Complete")

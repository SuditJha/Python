# return statement
# '''
# def mult(a,b):
#     return a*b
# x=int(input("Number : "))
# y=int(input("Number : "))
# -----------------------------------------------------
# z=mult(x,y)
# print(z)

# '''
#  ------------------------------------------------------
# Pass Statement

#  def a():
#      pass
#  ---------------------------------------------------------
#  Recursion

#  def fact(n):
#      if n==1:
#          return 1
#      else:
#          return n*fact(n-1)
    
#  n=int(input("Number : "))

#  print(fact(n))

#  ---------------------------------------------------------------------


#  binary to decimal

#  0b is the syntax for binary digit

 
# #a=int(0b1010)
# #b=int("1101",2)
# #c=int("0b1111",2)
# #print(a)
# #print(b)
# #print(c)
# #print(int(str(n),2))

#  0o is the suntax for octal numbers

# #a = int(0o100)
# #b = int("110", 8)
# #c = int("0o11", 8)
# #print(a)
# #print(b)
# #print(c)

#  0x is the suntax for octal numbers

# #a = int(0xB)
# #b = int("E", 16)
# #c = int("0x1A", 16)
# #print(a)
# #print(b)
# #print(c)

# # n = int(input("Number : "))
# #decimal to binary
# # a=bin(n)
# # print(a)

# #decimal to octal
# # b=oct(n)
# # print(b)

# #decimal to hexadecimal
# # c=hex(n)
# # print(c)

# #Dynamically typed :- same variable use for different purpose
# #P.S-- cannot be done in other programming languages like c, c++, java
# # decimal to binary
# # a = bin(n)
# # print(a)
# #decimal to octal
# # a = oct(n)
# # print(a)
# #decimal to hexadecimal
# # a = hex(n)
# # print(a)


# # Complex Numbers

# a=2+3j
# print(type(a))
# print("Real = ",a.real)
# print("Imaginary = ",a.imag)

# # Complex number using complex()

# a=complex(3,-5)complex() --> returns 0j
# print("COmplex Number = ",a)


# # Random number generation

# import random

# n=random.random()
# print("Random Number between (0,1)",n)

# # Random Integer Number

# n=random.randint(10,20)
# print("Random Integer Number between (10,20)",n)

# # Random in range with step value
# n=random.randrange(10,30,2)
# print("Random Number between (10,30,2)",n)

# # Random floating point number within given range
# n=random.uniform(10,40)
# print("Random Floating point Number between (10,40)",n)

# # List within given range
# n=random.sample(range(100,200),10)
# print("Random List of given numbers Number between (0,1)",n)

# # Shuffling from a list
# lst=[1,2,3,4,5,6]
# n=random.shuffle(lst)
# print(lst)

# # Random choosing from list

# n=random.choice(lst)
# print(n)

# lst=["mango","apple","guava","banana"]
# n = random.choice(lst)
# print(n)

# String Datatype

# name=input("Enter String : ")
# for x in name:
#     print(x)

# String slicing
# n="Hello, world"
# print(n[2:5])
# print(n[:6])
# print(n[4:])
# print(n[:])
# print(n[-5:-1])

n=input("Enter Name ")
print(n[2:6])
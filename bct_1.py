# 33 Keuwords in python

'''Bitwise Operators
9=  1001
7=  0111
---------
9&7=0001
9|7=1111
9^7=1110
'''
p = 9
q = 7
print(p & q)
print(p | q)
print(p ^ q)

n = int(input("Enter a  number : "))
if n > 5:
    print("Hi")
else:
    print("Bye")

n = int(input("Enter a  number : "))
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

n = int(input("Enter Age : "))

if n < 9:
    print(f"'Child'")
elif n > 18:
    print("'Adult'")
else:
    print("'Girl/Boy'")

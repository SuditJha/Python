# Write a program to count the total number of digits in a number.

n=int(input("Enter a number : "))
d=0
while n!=0:
    d+=1
    n=int(n/10)

print("Digits = ",d)
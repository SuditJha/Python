# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

n=int(input("Enter a number : "))
sum=0
for i in range(n+1):
    sum=sum+i
print(sum)
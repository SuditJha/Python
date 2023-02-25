# A company decided to give bonus of 5 % to employee if his/her year of service is more
# than 5 years.

salary=int(input("Enter Salary : "))
service=int(input("Enter Service : "))
bonus=0
if service>5:
    bonus = 5/100

print("Bonus = ",bonus*salary)


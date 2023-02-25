# class student:
#     def __init__(self,name,age,college):
#         self.name=name
#         self.age=age
#         self.college=college

# name=input("Enter your name ")
# age=input("Enter your age ")
# college=input("Enter your college ")

# s1=student(name,age,college)



# print("Name of Student : ",s1.name)
# print("Age of the Student : ",s1.age)
# print("College Name : ",s1.college)

# print()

# class student2:
#     def __init__(self, name, age, college):
#         self.name = name
#         self.age = age
#         self.college = college

#     def print(self):
#         print("Name of Student : ", name)
#         print("Age of the Student : ", age)
#         print("College Name : ", college)

# name=input("Enter your name ")
# age=input("Enter your age ")
# college=input("Enter your college ")

# print()

# s2=student2(name,age,college)
# s2.print()


# class student3:
#     def __init__(self, name, age, college):
#         self.name = name
#         self.age = age
#         self.college = college

#     def print(self):
#         print("Name of Student : ", self.name)
#         print("Age of the Student : ", self.age)
#         print("College Name : ", self.college)


# print()

# s3 = student3("Sudit",20,"NiT")
# s3.print()


# Inheritance

class person:
    def __init__(self,name,age,college):
        self.name=name
        self.age=age
        self.college = college
    
    def print(self):
        print("Name of Student : ", self.name)
        print("Age of the Student : ", self.age)
        print("College Name : ", self.college)


# Creating a child class
class student(person):
    def __init__(self, name, age, college,roll):
        super().__init__(name, age, college)
        # person.__init__(self,name,age,college)
        self.roll = roll
    
    def welcome(self):
        print("Welcome, ",self.name)

# p1 =student("Sudit", 20, "NiT")
# p1.print()
# print(p1.roll)

p2 = student("Arith",20,'JU',4321)
print("Name : ",p2.name)
print("Age : ", p2.age)
print("Coll : ", p2.college)
print("Roll : ",p2.roll)
print()
p2.welcome()

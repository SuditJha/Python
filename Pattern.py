# n=int(input("Enter rows : "))

# for i in range(n):
#     for j in range (n-i-1):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
'''
for i in range(n):#n=5
    for j in range(i):#j=0,0
        print(" ", end=" ")
    for j in range(n-i):#j=0,4
        print("*", end=" ")
    print()

str="Sudit"
l=len(str)

for i in range(l):
    for j in range (i+1):
        print(str[j]+" ",end="")
    print()
 
'''
for i in range(5):
    for j in range(i):
        print (j+1,end=" ")
    print()


        
    



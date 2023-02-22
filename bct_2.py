for i in range(1,5):
    print("*" * 4)

print()

for i in range(1, 5):
    print("*" * i)

print()

for i in range(1, 5):
    print("*" * (5-i))

print()

for i in range(5):
    for j in range(5-i):
        print(" ",end=" ")
    for j in range(i+1):
        print(" * ",end=" ")
    print()

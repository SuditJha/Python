# Write a program to create a tuple and multiply 5 with each element

t=(2,4,6,8)
tup=()
for x in t:
    s=5*x
    tup=tup+(s,)

print(tup)


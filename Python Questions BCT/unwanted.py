str=input("Enter string \n")

l=len(str)
n=''
for i in range(l):
    c=str[i]
    if c.isalpha():
        n=n+c
    elif c.isnumeric():
        n=n+c
    else:
        continue

print(n)
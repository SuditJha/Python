n=int(input("Number: "))
def fact(x=1):
    if(x<=1):
        return 1
    else:
        return x*fact(x-1)
print(fact(n))
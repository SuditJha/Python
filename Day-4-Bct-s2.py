# List Comprehension

car=['bugati','toyota','bmw','nissan','thar','ferrari']
nc=[x for x in car if 't' in x]
print(nc)

x=[]
for i in range (5):
    a=int(input("Number"))
    x.append(a)

x.sort()
print(x[0],x[-1])
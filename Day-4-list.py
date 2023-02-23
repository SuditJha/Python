# # Lists
# l=['apple','cherry',1,3,5,'apple']
# print(len(l))
# print(type(l))

# # Access the list

# for i in l:
#     print(i)
# print()
# for i in range(len(l)):
#     print(l[i])

# print(l[1:])
# print(l[:4])
# print(l[-1])
# print(l[-3:-1])
# # changing list items in range
# l[1:3]=['bmw','tree']
# print(l)

# # Adding an element in list use insert(position,value) 
# l.insert(2,'Guava')
# print(l)
# l.insert(1,234)
# print(l)


# l=['apple','cherry','grapes','cherry']
# l[3]='mango'
# l.insert(2,'watermelon')
# print(l)

# l=['apple','cherry','grapes','mango']
# l.append('kiwi')
# print(l)
# # extend() method works with any iterable i.e list ,tuple
# l2=['red','blue','green']
# l.extend(l2)
# print(l)

# # remove() -> remove specific element

# l.remove('kiwi')
# print(l)

# # pop() -> default-remove fro last or you can mention index to pop(4)
# print(l.pop())
# print(l)

# print(l.pop(0))
# print(l)


l=['apple','cherry','grapes','cherry']
# l.remove('cherry')
# l.pop()
# print(l)

# del keyword delete an item or delete the whole list

del l[1]
print(l)

# Clearing the list -- clear() -> returns empty list

l.clear()
print(l)

# del l
# after deleting list on printing it gives error
# print (l)
# NameError: name 'l' is not defined

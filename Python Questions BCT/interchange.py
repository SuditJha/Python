# Program to interchange first and last element of a list and then print the list.

lst=['apple','mango','guava','cherry','grapes','kiwi']

print(lst)

l = len(lst)
c=lst[0]
lst[0]=lst[l-1]
lst[l-1]=c

print(lst)


# Program to show various ways to
# write data to a file using with statement

L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]

# Writing to file
with open("myfile.txt", "w") as file1:
	# Writing data to a file
	file1.write("Hello \n")
	file1.writelines(L)

# Reading from file
with open("myfile.txt", "r") as file1:
	# Reading form a file
	print(file1.read())

with open("orignal.txt","r") as f:
    a=f.read()
    print(f.read())

with open("copy.txt","w") as w:
    w.write("The line from Orignal.txt\n")
    w.write(a)
with open("copy.txt","r") as c:
    x=c.read()
    print(x)
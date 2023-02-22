#no. of guesses=9
#print no. of guesses left
#no of guesses he took to finish
#game over
n=18
g=1
num=int(input("enter your guessing number: "))
while(g<=9):
    if(num==n):
        print("correct guess",num)
        break
    if(num>n):
        print("guess lower no.")
    g=g+1
    print("no. of guess is left: ",g)
    else:
        print("guess higher no.")
        g=g+1
        print("no. of guess is left: ", g)
            


import random

#random = Random;
#generate a random number
compNum = random.randint(1,10)
#bool variable for while loop
win = False
#while loop to allow for multiple guesses
while (win!=True):
    print ('Choose a number between 1-10')
    #get user input
    myNum = int(input())
    #print (compNum)
#if statements to processes different information for user
    if (myNum<compNum):
        print('Too low')
    elif (myNum>compNum):
        print('Too high)')
    else:
        print ('You guessed the number')
        win = True;

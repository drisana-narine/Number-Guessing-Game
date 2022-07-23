import random

def validDigit(digit):
    #checks that number of digits is within range
    while not(digit>=1 and digit<=10):
        print("This number is not between 1 and 10")
        digit=int(input("Please enter the number of digits (between 1 and 10) of the number: "))
        #makes user reenter number if it is not between 1 and 10 (inclusive)
    return digit

def generateNum(numDigits):
    #generates random number 1 by 1
    current=0
    strNum=""
    digit=str(random.randrange(0,10))
    while current<numDigits:       
        if strNum.count(digit)==0:
            #checks for repeating digits
            strNum=strNum+digit
            digit=str(random.randrange(0,10))
            current=current+1
        else:
            digit=str(random.randrange(0,10))
            #assigns different number to digit if the number repeats
    return strNum

def validate(theGuess,digit,x):
    i=0
    while i<len(theGuess):
        if len(theGuess)!= digit:
            #checks that the guess is the correct length
            print("The number of digits in your guess does not match the number of digits you entered earlier.")
            print("What is your valid guess #"+str(x)+" of this "+str(digit)+"-digit number?")
            theGuess=input("Guess: ")
            #makes user enter another guess if it is not the right length
        elif theGuess.count(theGuess[i])>1:
            #checks for repeating digits
            i=0
            print("You can't enter duplicate digits.")
            print("What is your valid guess #"+str(x)+" of this "+str(digit)+"-digit number?")
            theGuess=input("Guess: ")
            #makes user enter another guess if there are repeating digits
        else:
            i=i+1
    return theGuess

def check1(guess,num):
    #checks for any digits in the right place
    i=0
    A=0
    #A keeps track of digits in the right place
    while i<len(num):
        if guess[i]==num[i]:
            #compares numbers character by character
            A=A+1
            i=i+1
        else:
            i=i+1
    return str(A)+"A"

def check2(guess,num):
    #checks for any right digit in the wrong place
    i=0
    B=0
    #B keeps track of correct digits in the wrong place
    while i<len(num):
        if num.count(guess[i])==1 and guess[i]!=num[i]:
            #checks to see if character is in the number and in the wrong place
            B=B+1
            i=i+1
        else:
            i=i+1
    return str(B)+"B"
    
def main():
    digit=int(input("Please enter the number of digits (between 1 and 10) of the number: "))
    print("The number in front of A means digits in the correct place, the number in front of B means correct digit that are nor in the the correct place.")
    #user enters length of the random number
    digit=validDigit(digit)
    #makes sure digit is not less than 1 or greater thhan 10
    num=generateNum(digit)
    guess=0
    guessNumber=1
    #keeps track of the number of valid guesses
    while guess!=num:
        #stays in loop until guess is correct
        print("What is your valid guess #"+str(guessNumber)+" of this "+str(digit)+"-digit number?")
        guess=input("Guess: ")
        #user enters guess
        guess=validate(guess,digit,guessNumber)
        #checks if user's guess is valid
        rightPlace=check1(guess,num)
        rightNum=check2(guess,num)
        if guessNumber==7 and guess!=num:
            #exits loop so user only gets 7 tries
            guess=num
            print("You ran out of guesses. The number was "+num)
            print("Game Over")
        elif rightPlace+rightNum=="0A0B":
            #prints nothing if there are no correct digits 
            print("Nothing")
            guessNumber=guessNumber+1
        elif guess==num:
            #congratulates user when they guess correctly
            print("Congrats! You only took",guessNumber,"valid guesses to get "+num+".")
        elif rightPlace=="0A":
            #prints number of correct digits when no digits are in the right place
            print("Your guess generated "+rightNum+".")
            guessNumber=guessNumber+1
        elif rightNum=="0B":
            #prints number of correct digits in the right place no correct digits are in the wrong place
            print("Your guess generated "+rightPlace+".")
            guessNumber=guessNumber+1
        elif guess!=num:
            #prints number of correct digits and correct digits in correct places
            print("Your guess generated "+rightPlace+rightNum+".")
            guessNumber=guessNumber+1
            
main()

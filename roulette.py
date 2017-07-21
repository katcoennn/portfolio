import random
from random import randint

answerNum = (randint (1,36))
color = ["red", "black"]
answerColor = random.choice (color)
answerColor = str(answerColor)
money = int(input("How much money would you like to start the game with? "))
bet = int(input("How much money would you like to bet? "))
guessNum = input("Guess a number between 1 and 36: ")
guessColor = str(input("Guess the color- red or black: "))

print ("")
if guessNum == answerNum and guessColor == answerColor:
    print ("It was an exact answer! Good job!")
    money += (bet*5)
else:
    if guessNum == answerNum:
        print ("You guessed the correct number, but the correct color was "+answerColor+"!" )
        money += bet
    else:
        print ("You guessed the wrong number. The answer was "+(str(answerNum))+"!")
        money -= bet

    if guessColor == answerColor:
        print ("You guessed the correct color!")
        money += bet
    else:
        print ("You guessed the wrong color! The correct color was "+(str(answerColor))+"!")
        money -= bet

    if (int(guessNum) % 2 == 0) and (int(answerNum) % 2 == 0) :
        print ("Your guess and the answer were both even!")
        money += bet
    elif (int(guessNum) % 2 == 1) and (int(answerNum) % 2 == 1):
        print ("Your guess and the answer were both odd!")
        money += bet
    elif (int(guessNum) % 2 ==0):
        print ("Your guess was even but the correct number was odd!")
        money -= bet
    else:
        print ("Your guess was odd but the correct number was even!")
        money -= bet

print ("You walk away with "+(str(money))+ " dollars!")

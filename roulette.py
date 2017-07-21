import random
from random import randint
import sys
money = 3
money = int(input("How much money would you like to start the game with? "))
bet = int(input("How much money would you like to bet? "))

def hardone(answerNum, guessNum, guessColor, answerColor, money):
    if guessNum == answerNum and guessColor == answerColor:
        print ("It was an exact answer! Good job!")
        money += (bet*5)
def numMatch(answerNum, guessNum, money):
    if guessNum == answerNum:
        print ("You guessed the correct number, but the correct color was "+answerColor+"!" )
        money += bet
    else:
        print ("You guessed the wrong number. The answer was "+(str(answerNum))+"!")
        money -= bet
def colorMatch(guessColor, answerColor, money):
    if guessColor == answerColor:
        print ("You guessed the correct color!")
        money += bet
    else:
        print ("You guessed the wrong color! The correct color was "+(str(answerColor))+"!")
        money -= bet
def parity(answerNum, guessNum, money):
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
if money <= 0:
    print ("You're too broke to play, son")
    sys.exit()
if bet > money:
    print ("You're too broke to play, son")
    sys.exit()
while money > 0:
    answerNum = (randint (1,36))
    color = ["red", "black"]
    answerColor = random.choice (color)
    answerColor = str(answerColor)
    guessNum = input("Guess a number between 1 and 36: ")
    guessColor = str(input("Guess the color- red or black: "))
    print ("")

    print ("What game do you want to play?")
    print ("Press 1 to bet on an exact match.")
    print ("Press 2 to bet on a number match.")
    print ("Press 3 to bet on a color match.")
    print ("Press 4 to bet on a parity match.")
    print ("Type all numbers straight through. For example, to place all bets, type 1234 and hit enter.")
    user_input = input()
    if "1" in user_input:
        hardone(answerNum, guessNum, guessColor, answerColor, money)
    if "2" in user_input:
        numMatch(answerNum, guessNum, money)
    if "3" in user_input:
        colorMatch(guessColor, answerColor, money)
    if "4" in user_input:
        parity(answerNum, guessNum, money)
    print ("You now have "+(str(money))+ " dollars!")

sys.exit()

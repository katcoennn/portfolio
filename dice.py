from random import randint
dice = randint (1,6)
guess = str(input("Guess a number between 1 and 6!"))
answer = str(dice)
if guess == answer:
    print ("You are correct! The dice rolled the number "+answer+"!")
else:
    print ("You are incorrect! You guessed "+guess+" but the dice rolled "+answer+"!")

import random
dice = [1,2,3,4,5,6]
a = (random.choice(dice))
print ("What number will the dice roll?")
user_input = input()
if user_input == a:
    print ("You are correct! The dice rolled the number "+a+"!")
else:
    print ("You are incorrect! The dice rolled the number "+a+"!")

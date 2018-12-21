#Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:
#
#1. If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
#2. On a player's first turn, if their guess is
# * within 10 of the number, return "WARM!"
# * further than 10 away from the number, return "COLD!"
#3. On all subsequent turns, if a guess is 
# * closer to the number than the previous guess return "WARMER!"
# * farther from the number than the previous guess, return "COLDER!"
#4. When the player's guess equals the number, tell them they've guessed correctly *and* how many guesses it took!

from random import randint
number = randint(1,100)

print("Try to guess the number from 1 to 100")
guesses = [0]

print(number)

while True:

    user_num = int(input("Type your number: "))
    guesses.append(int(user_num))
    
    if user_num == number:
        print("You've guessed the number!")
        if len(guesses) == 2:
            print('You had 1 guess')
        else:
            print("You had {} guesses!".format(len(guesses)-1))
        break
    elif user_num < 1 or user_num > 100:
        print("Out of range! Try again!")
    elif len(guesses) == 2:
        if number - user_num <=10:
            print("WARM!")
        else:
            print("COLD!")
    else:
        if guesses[-2] - user_num <=10:
            print("WARMER!")
        else:
            print("COLDER!")

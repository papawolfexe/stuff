import random
secretnumber = random.randint(1, 10)

secretnumber_guess = input("Guess the secret number\n:")
print("Your guess was " + secretnumber_guess)
if secretnumber_guess == str(secretnumber):
    print("Congrats the secret number was " + str(secretnumber))
elif secretnumber_guess == str(secretnumber + 2) or secretnumber_guess == str(secretnumber - 2):
    print("So close, you were within 2 of the secret number, the number was " + str(secretnumber))
elif secretnumber_guess == str(secretnumber + 1) or secretnumber_guess == str(secretnumber - 1):
    print("So close, you were within 1 of the secret number, the number was " + str(secretnumber))
else:
    print("That is not the right number, the secret number was " + str(secretnumber))

question = input("So did you get the secreat number?\n")
if question == "yes" and secretnumber_guess != secretnumber:
    print("Dont Lie, you guessed " + str(secretnumber_guess) + " but the number was " + str(secretnumber))
elif question == "yes" and secretnumber_guess == secretnumber:
    print("Wow your good at guessing")
elif question == "no":
    print("Not a suprise, guessing 1 - 10 is pretty unlikely")
else:
    print("What?")
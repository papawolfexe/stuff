# Random Number Generator
import random
numbers = random.randint(1,10)

# Number Guesser
random_number_guess = int(input("What do you think the random number is?\nrange: (1, 10)\n"))
if numbers == random_number_guess:
    print("Congratulations that was the correct number!")
elif numbers == (random_number_guess + 1) or numbers == (random_number_guess - 1):
    print("Very close but no cigar")
else:
    print("You suck try again later")
    exit()
import random
import math

# Taking inputs from users
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))
 
# generating random number between the lower and upper
x = random.randint(lower, upper)

#total number of gusses basesd on upper and lower number
number_of_guesses = round(math.log(upper - lower + 1, 2))

print(f"You have {number_of_guesses} chances to guess the number!\n")
 
# Initializing the number of guesses.
guess_count = 0
 
# for calculation of minimum number of guesses depends upon range
while guess_count < number_of_guesses:
    guess_count += 1
 
    # taking guessing number as input from user
    guess = int(input("Guess a number:- "))
 
    # Condition testing
    if x == guess:
        print("Congratulations 😎 you guessed the number on ",
              guess_count, " try")
        # Once the number is guessed, loop will break or stop
        break
    elif x > guess:
        print("You guessed too small!")
    elif x < guess:
        print("You Guessed too high!")
 
# If Guessing is more than from the required number_of_guesses,
if guess_count >= number_of_guesses:
    print(f"You tried {number_of_guesses} guesses!")
    print(f"\nThe number is {x}")
    print("Just Try again!😊")
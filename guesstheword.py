import random
# library that we use in order to choose on random words from a list of words

name = input("Enter your name? :")
# Here the user is asked to enter name

print("Best of luck ! ", name)

words = ['python', 'pandas', 'statistics', 'programming',
		'java', 'mathematics', 'data', 'numpy',
		'javascript', 'typescript', 'nodejs', 'sql']

# will choose one random word from list of words
word = random.choice(words)


print("Now Guess the characters in word")

guesses = ''

# any number of turns can be used here
turns = 12


while turns > 0:

	# counts the number of times a user fails
	failed = 0

	# all characters from the input word taking one at a time.
	for char in word:

		# comparing that character with the character in guesses
		if char in guesses:
			print(char, end=" ")

		else:
			print("_")
			#print(char, end=" ")

			# for every failure 1 will be incremented
			failed += 1

	if failed == 0:
		# user will win the game if failure is 0 and 'You Win' will be given as output
		print("Hey! you Win ")

		# this print the correct word
		print("The guesses word is: ", word)
		break

	# if user has input the wrong alphabet then it will ask user to enter again
	print()
	guess = input("guess the character:")

	# every input character will be stored in guesses
	guesses += guess

	# check input with the character in word
	if guess not in word:

		turns -= 1

		# if the character doesn’t match the word then the following will be given as output
		print("Wrong guess")

		# this will print the number of turns left for the user
		print("You have", + turns, 'to guesses the word!')

		if turns == 0:
			print("You Loose the game !!!!!")

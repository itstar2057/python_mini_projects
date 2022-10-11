import random

num = random.randint(1, 10)
guess = None

while guess != num:
    guess = input("guess the number 1 to 10 : ")
    guess = int(guess)

    if guess == num:
        print(f"congratulations! you guess the number = {num}!")
        break
            
    else:
        print("wrong guess,  try again!")
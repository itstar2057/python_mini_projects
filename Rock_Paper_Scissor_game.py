import random

User = input("Select Rock, Paper, or Scissor :=> ").lower()
Computer = random.choice(["Rock", "Paper", "Scissor"]).lower()
print("Computer selected:=> ", Computer)

if User == "rock" and Computer == "paper":
    print("Computer Won")
elif User == "paper" and Computer == "scissor":
    print("Computer Won")
elif User == "scissor" and Computer == "rock":
    print("Computer Won")
elif User == Computer:
    print("Tie")
else:
    print("User Won")
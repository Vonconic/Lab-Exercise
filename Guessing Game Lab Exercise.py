import random

correct_answer = random.randint(1,10)

guess_amount = 0

player_name = input("What is your name:")

print(f"Hello {player_name}, Guess a number between 1 and 10")

#Runs the code while the guess amount it less than three
#Each guess increases the current guess amount
#Checks to see if the players guess is the correct answer or if it is higher or lower

while guess_amount < 3:
    player_guess = int(input("Enter your guess:"))
    guess_amount = guess_amount + 1
    if player_guess == correct_answer:
        print(player_name, "You won!")
        break
    elif player_guess < correct_answer:
        print(f"{player_guess} is too low")
    else:
        print(f"{player_guess} is too high")
if player_guess != correct_answer:
    print(f"Game Over. The number was {correct_answer}")
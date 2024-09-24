import random

number_to_guess = random.randrange(100)

GUESS_CHANCES = 7
current_chance = 0

while current_chance < 7:
    user_ip = int(input("What's your guess?!"))
    current_chance += 1
    if user_ip == number_to_guess:
        print(f"Hurray!! You guessed right in {current_chance} try!!")
        break
    elif current_chance >= GUESS_CHANCES and user_ip != number_to_guess:
        print("Oops!! You've exhausted all the chances! Better luck next time")
    elif user_ip < number_to_guess:
        print("Too small! Try again")
    elif user_ip > number_to_guess:
        print("Too high! Try again")

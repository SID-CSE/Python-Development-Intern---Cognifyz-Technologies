#Level 2 :Task 2
#Task: Number Guesser
'''
 Create a number guessing game where the program generates a random number between a specified range, and the user
 tries to guess it.Provide feedback to the user if their guess is too high or too low.
'''

import random

def number_guesser():
    while True:
        try:
            start = int(input("Enter the starting number of the range: "))
            end = int(input("Enter the ending number of the range: "))
            if start >= end:
                print("Starting number must be less than ending number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

    random_num = random.randint(start, end)
    attempts = 1

    while True:
        try:
            guess_num = int(input(f"Guess a number between {start} and {end}: "))
            if guess_num < start or guess_num > end:
                print(f"Please enter a number within the range {start} to {end}.")
                continue

            if guess_num < random_num:
                print("You are too low")
            elif guess_num > random_num:
                print("You are too high")
            else:
                print(f"You are correct, The Number is {guess_num}")
                print(f"You achieved the number in {attempts} steps")
                break

            attempts += 1
        except ValueError:
            print("Invalid input. Please enter a valid number.")

number_guesser()

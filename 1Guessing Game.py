#Level 2 :Task 1
#Task: Guessing Game
'''
 Create a number guessing game where the program generates a random number between a specified range,
 and the user tries to guess it.
 Provide feedback to the user if their guess is too high or too low.
'''
import random

def guessing_game():
    random_num = random.randint(1, 100)
    attempts = 1
    while True:
        try:
            guess_num = int(input("Enter the number you guess (1-100): "))
            if guess_num < 1 or guess_num > 100:
                print("Please enter a number within the range 1 to 100.")
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

guessing_game()
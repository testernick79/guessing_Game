import random


def get_prompt():
    """
    Prompts the user to input a number from 1-20,
    and validates if the input is proper or not.
    If the input is not correct, it will prompt the user to try again.
    Returns the validated number.
    """
    while True:
        prompt = input("Please enter a number from 1-20: ")
        try:
            guess = int(prompt)
            if guess < 1 or guess > 20:
                raise ValueError("Number not in range!")
        except ValueError:
            print("Wrong input. Try again!")
        else:
            return guess


def guess_number(number):
    """
    Receives a number and asks the user to try and guess the number.
    Once guessed, it returns the number of tries it took the user to
    guess the number.
    """
    tries = 0
    number = number

    while True:
        guess = get_prompt()

        if guess < number:
            print("The correct number is higher!")
            tries += 1
        elif guess > number:
            print("The correct number is lower!")
            tries += 1
        elif guess == number:
            tries += 1
            print("Correct!")
            return tries


def generate_number():
    """
    Generates a random number between 1 - 20 and returns it.
    """
    number = int(20 * random.random())
    if number == 0:
        number += 1

    return number


def start_game():
    """
    Starts the Number Guessing Game.
    """
    print("""
====================================
Welcome to the Number Guessing Game!
      Good Luck and Have Fun!
====================================
""")

    high_score = 0
    current_score = 0
    number = generate_number()

    while True:
        tries = guess_number(number)
        current_score = tries
        print("Number of attempts: {}".format(tries))

        if high_score == 0:
            high_score = current_score
        elif current_score < high_score:
            high_score = current_score

        while True:
            play_again = input("Would you like to play again? Yes(y)/No(n)? ")

            if play_again == 'y':
                print("Generating new number...")
                number = generate_number()
                print("Your Current High Score is: {}".format(high_score))
                break
            elif play_again == 'n':
                print("Thanks for playing! Goodbye!")
                break
            else:
                print("Wrong input. Try again!")
                continue

        if play_again == 'n':
            break


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()

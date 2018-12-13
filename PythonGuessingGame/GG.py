# Python Number Guessing GAME
# REQUIREMENTS

# If they choose correctly display they got it, and tell them the number guessed and the number it was as well as how many tries
# After the game is done the user can enter a new game.
# a new randome number is generated.
# limit the number of tries to 5
import random


# Generate a random number from 1,20
def randomNumber():
    magic_number = random.randint(1, 15)

    # Any user can return and use the Magic number returned
    return magic_number


# Prompt the user to ask for the number they want to choose
def userNumbers(message="Pick a Number: "):
    user_answer = (input(message))

    # Any user can return and use the user answer returned
    return user_answer


# If the number is too high, tell them  it is too high and try again
# If the number is too low, tell them  it is too low and try again
def checkUserNumber(user_answer, magic_number):
    if user_answer > magic_number:
        print("too high , try again")
    elif user_answer < magic_number:
        print("too low , try again")
    else:
        # you have to use a format string to fill in `user_answer` and `magic_number`
        # with their actual value.
        print("Great Guess! you chose user_answer, and the correct answer was magic_number, with only (number of tries!)")


# Start the game
def main():

    # 1. Welcome the user to the game
    print("""
    ===============================================
            Welcome to the Guessing Game
    ===============================================""")

    # 2. Store a variable -
           #1a. (i choose this number)
           #1b. (generated number)
    answer = randomNumber()
    print(answer)
    # 3. keep prompting user for a guess
    attempt = True

    while attempt:

        # validate a number between 1 - 15 that user selects

            try:

                    guess = int(input("Please enter a number: "))
            except ValueError:
                    print("--NOT-- a Number!, Try again: ")
                    continue

        # once a valid guess is selected, we need to compare
        # if the guess is less than answer
            if guess < answer:
                print("---------------------TOO LOW!---------------------")

            # also if guess is greater than answer
            elif guess > answer:
                print("---------------------TOO HIGH!---------------------")

            # finally if guess is exactly equal to answer

            else:
                print("---------------------Great guess!---------------------")
                print("It was {} and you guessed {}".format(answer, guess ))
                again =  input("Play Again (Y/N?): ")
                attempt = False

                if again.lower() == "y":
                    main()
                if again.lower() == "n":
                    print("""
    ===============================================
                        GAME OVER
                    Thanks For Playing!!
    ===============================================""")
                    break

main()

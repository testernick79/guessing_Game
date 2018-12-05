# Python Number Guessing GAME
# REQUIREMENTS

# If they choose correctly display they got it, and tell them the number guessed and the number it was as well as how many tries
# After the game is done the user can enter a new game.
# a new randome number is generated.
# limit the number of tries to 5
import random


# Generate a random number from 1,20
def randomNumber():
    magic_number = random.randint(1, 20)

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
        print("Great Guess! you chose user_answer, and the correct answer was magic_number, with only tries!")


# Start the game
def main():
    user_success = False
    start_game = True

    # if either are true game will run

    i = 1  # DEBUG COUNTER
    while user_success or start_game:
        # DEBUG PRINT - using DEBUG COUNTER
        print("Main loop is running: {}".format(i))

        user_answer = userNumbers()
        magic_number = randomNumber()
        
        message = checkUserNumber(user_answer, magic_number)

        # DEBUG PRINTING VARIABLES
        #print("-----------------------------")
        #print("user_answer is: ", user_answer)
        #print("magic_number is: ", magic_number)
        #print("number_chosen is: ", number_chosen)
        #print("-----------------------------")

        # the 1st argument will go into checkUserNumber as `user_answer` when inside that function.
        # the 2nd argument will go into checkUserNumber as `magic_number` when inside that function.
        message = checkUserNumber(user_answer, randomNumber)
        # display a message when the user guesses correct.
        while message != "Great Guess!":
            print(message)
            number_chosen = userNumbers("Please Try Again!: ")
            message = user_answer(user_answer, randomNumber)
            
        print(message)
        user_success = True

main()

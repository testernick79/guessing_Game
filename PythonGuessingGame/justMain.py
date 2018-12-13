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
            message = checkUserNumber(user_answer, randomNumber)

        print(message)
        user_success = True

main()

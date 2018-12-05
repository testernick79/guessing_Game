import random

#-------------------user_response define variables---------------------------
def user_response():

        """
        Prompt the user to select a number between 1, 20
        If the user selects a number a number outside the scope.
        A try again message will be displayed
        """

        while True:
            prompt = input("Choose a number from 1 - 20: ")
        try:
            user_guess = int(promt)
            if user_guess < 1 or user_guess > 20:
                raise ValueError("Your guess needs to be: /b - More than 0 and less than 20 ")
        except ValueError:
            print("----------------------* *Not a valid response. Try again!* *----------------------")
        else:
            return user_guess

#-------------------guess_number function---------------------------
def guess_number(number):
    """
    recieves a number and asks the user to gues what that number is.
    Also show how many attempts.
    """
    tries = 0
    number = atempt_number

    while True:
        user_guess = user_response()

        if user_guess < number:
            print("<--------------------------->Select a Higher Number!<--------------------------->")
            tries += 1

        elif user_guess > number:
            print("<--------------------------->Select a Lower Number!<--------------------------->")
            tries += 1

        elif user_guess == number:
            tries += 1
            print("<--------------------------->GREAT GUESS!<--------------------------->")
            return tries

#-------------------generate_secret_number function---------------------------
    def generate_secret_number():
        """
        Generates a super secret number,
        between 1 - 20 and returns
        """

    number = int(20 * random.random())
    if number == 0:
        number += 1
        return number

def start_game():
    print("""
========================================
            Lets Play a Game!    
                    
========================================     
     
""")

    best_score = 0
    your_score = 0
    number = generate_secret_number()

    while True:
        tries = guess_number(number)
        your_score = tries
        print("Attempts:  {}".format(attempts))

        if best_score == 0:
            best_score = your_score

        elif your_score < best_score:
            best_score = your_score

    while True:
        keep_playing = input("Lets Play Again! YES(y)/NO(n) ?")
        if keep_playing == 'y':
            print("Game Refreshing")
            print(".")
            print("..")
            print("...")
            print("....")
            print(".....")
            print("....")
            print("...")
            print("..")
            print(".")
            number = generate_secret_number()
            print("Best score was: {}".format(best_score))


        elif keep_playing == 'n':
            break
            print("Thanks for playing! Come back soon!")


        else:
            print("OOOPS, Wong response. Try Again!")
            continue

        if keep_playing == 'n':
            break



if __name__ == '__main__':
    #Start the game
   start_game()

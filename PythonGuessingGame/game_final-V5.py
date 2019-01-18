import random
import sys

def print_welcome():
    # 1. Welcome the user to the game
    print("""
    ===============================================
            Welcome to the Guessing Game
    ===============================================""")

def print_guessing_game():
    print("""
    ********************   GUESSING GAME   ********************
    Enter a number between 1 and 8:""")


def prompt_user():
    '''- prompt the user for a number, Handle invalid values
       - Store a message, return a stored value entered
    '''
    while True:

          try:
            guess = int(input())
            if guess < 1 or guess > 8:
                 raise ValueError("Enter A Value Between 1, and 8, Try again : ")
          except ValueError:
           print(" !!Enter a NUMBER 1 - 8,  Try Again!! :")



          else:
              print("TEST PRINT")
              return guess

def number_gen():
    '''
    - Create a Random Generated Number between 1 - 8

    '''
    magic_number = random.randint(1, 8)
    if magic_number == 0:
        magic_number += 1

    return magic_number


def play_again():

 # - Create a way to play again once the game ends

    keep_playing = input(" Do you want to continue playing? : \n").lower()


    if keep_playing.lower() in ['y', 'yes']:


        print(" ------- **Generating A New Random Number** -------")
        one_game()
        return True

    elif keep_playing.lower() in ['n', 'no']:


        sys.exit("""
        ===============================================
                    THANKS FOR PLAYING!!
        ===============================================            
        """)




    else:
        print(" Please enter 'yes' or 'no' ")
        play_again()




def one_game():
    # STEP 1
    print_welcome()
    # STEP 2
    print_guessing_game()
    # STEP 3
    trys = 0

    magic_number = number_gen()
    keep_playing = True
    while True:

        my_guess = prompt_user()
        trys += 1


        if my_guess < magic_number:
            print(" ** TOO LOW!! ** :")


        elif my_guess > magic_number:
            print(" ** TOO HIGH!! ** :")


        else:

            print("""
            =======================
            GOOD JOB IT WAS:\n
            {}
            YOU GUESSED:\n
            {}
            WITH {} TRIES
            ======================""".format(magic_number, my_guess, trys))

            play_again()







if __name__ == '__main__':
    # Play the game Onetime
    one_game()
    # Continue to play the game
    play_again()

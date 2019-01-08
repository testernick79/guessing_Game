import random

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

def one_game():
    # STEP 1
    print_welcome()
    # STEP 2
    print_guessing_game()
    # STEP 3
    trys = 0
    magic_number = number_gen()
    while True:

        my_guess =prompt_user()

        if my_guess < magic_number:
            print(" ** TOO LOW!! ** :")
            trys += 1

        elif my_guess > magic_number:
            print(" ** TOO HIGH!! ** :")
            trys += 1

        else:
            print("""
            =======================
            GOOD JOB IT WAS:\n
            {}
            YOU GUESSED:\n
            {}
            WITH {} TRIES
            ======================""".format(magic_number, my_guess, trys))
            return magic_number
    # STEP 4



if __name__ == '__main__':
    one_game()
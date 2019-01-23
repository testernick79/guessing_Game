import random

def prompt_user(message = "Pick a Number From 1 - 8:    "):
    '''- prompt the user for a number, Handle invalid values
       - Store a message, return a stored value entered
    '''
    while True:

          try:
            guess = int(input(message))
            if guess < 1 or guess > 8:
                 raise ValueError("Enter A Value Between 1, and 8, Try again:  ")
          except ValueError:
              print("Needs To Be a Number Above 0, Try Again")

          else:
              print("TEST PRINT")
              return guess


def user_guess(magic_number):
    print("PRINT X3")
    '''
    - Gets a number then asks the user for a guess
    - Then returns tries
    '''
    attempts = 0
    magic_number = magic_number


    while True:
        my_guess = prompt_user()


        if my_guess < magic_number:
            print("--------- *TOO LOW!!* ---------\n")
            attempts += 1
            print("PRINT X3.1")

        elif my_guess > magic_number:
            print("--------- *TOO HIGH!!* ---------\n")
            attempts += 1
            print("PRINT X3.2")

        else:

            print("""
    ===============================================
            GOOD JOB IT WAS:\n 
            {} 
            YOU GUESSED:\n 
            {}
            WITH {} TRIES
    ===============================================""".format(magic_number, my_guess, attempts))
            print("PRINT X3.3")
            play_again()

def number_gen():
    '''
    - Create a Random Generated Number between 1 - 8

    '''
    magic_number = random.randint(0, 8)
    if magic_number == 0:
        magic_number += 1
    return magic_number

# print a welcome to the user on game start
def print_value_error():
    print("Needs To Be a Number Positive, Try Again")

def print_welcome():
    print("""
    ===============================================
            Welcome to the Guessing Game
    ===============================================\n""")

def print_come_back():
    print("""                                          
    ===============================================    
          THANKS FOR PLAYING, COME BACK SOON               
    ===============================================\n""")

def print_attempts():
    attempts = 0
    print("You attempted: {} Times".format(attempts))

def print_y_n_error():
    print("Please Enter 'Yes' or 'No':\n  " )


'''
gets numbers entered by user
'''
def get_numbers():

    while True:
        try:

            guess = int(input("Enter a number:  "))
        except ValueError:
            print("--NOT-- a Number!, 1,10, etc. Try Again:\n   ")

        else:
            return guess

def play_again():
    try_again = input(" Do you want to play again Y/N:?    \n").lower()

    if try_again in ['y', 'yes']:
        return True

    elif try_again in ['n', 'no']:
        return False

    else:
        print_y_n_error()

def game_start():
    '''
    STEPS:
    * * ATTENTION * * READ ME
    1 - welcome the user    √ DONE
    2 - Generate a number   √ DONE
    3 - Ask Player for a Number     √ DONE
    4 - Print either too high or too low    √ DONE
    5 - Print success message if they guess right and attempts  √ DONE
    6 - play_again() kicks off after number is guessed  √ DONE
    '''
    # STEP 1

    print_welcome()

    your_score = 0
    attempts = 0
    number = number_gen()

    while True:
        print("game_start while true TEST PRINT")
        keep_playing = True
        print("PRINT 1X2")
        tries = user_guess(number)
        print("PRINT X2")
        your_score = attempts
        print_attempts()
        print("PRINT X3")

        if your_score == 0:
           your_score = attempts

        elif your_score < attempts:
            attempts = your_score
            print("TEST PRINT")

        while  True:

                keep_playing = input(" Do you want to play again Y/N:?    \n").lower()

                if keep_playing == ['y', 'yes']:
                        print(" ------- **Generating A New Random Number** -------")
                        play_again()
                        print_attempts()
                        break

                elif keep_playing == ['n', 'no']:
                        print_come_back()
                        break

                else:
                        print_y_n_error()
















if __name__ == '__main__':
    game_start()

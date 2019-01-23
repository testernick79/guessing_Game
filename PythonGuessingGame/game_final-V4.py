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
            return my_guess


def number_gen():
    '''
    - Create a Random Generated Number between 1 - 8

    '''
    magic_number = random.randint(1, 8)
    if magic_number == 0:
        magic_number += 1
    return magic_number


#---------------------- **PRINTING FUNCTIONS** ----------------------*START

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


#---------------------- **PRINTING FUNCTIONS** ----------------------*END



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

    print("I'm ALIVE!!!")

    keep_playing = input(" Do you want to play again Y/N:?    \n").lower()

    if keep_playing == ['y', 'yes']:
                        print(" ------- **Generating A New Random Number** -------")
                        play_again()
                        print_attempts()


    elif keep_playing == ['n', 'no']:
        print_come_back()


    else:
                    print_y_n_error()


def one_game():
    '''
    STEPS:
    * * ATTENTION * * READ ME



    4 - Print either too high or too low    √ NOT-DONE
    5 - Print success message if they guess right and attempts  √ NOT-DONE
    6 - play_again() kicks off after number is guessed  √ NOT-DONE
    '''

    # STEP 1
    #1 - welcome the user    √ DONE
print_welcome()
    # STEP 2
    #2 - Create Random Number    √ DONE
the_number = number_gen()
    # STEP 3
    #3 - Prompt for the users guess    √ DONE
prompt_user()
    # STEP 4
    #4 - Compare then display too high or too low √ DONE
user_guess()








if __name__ == '__main__':
    one_game()

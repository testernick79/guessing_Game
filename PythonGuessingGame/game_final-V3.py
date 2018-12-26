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
              print("Needs To Be a Number, Try Again")

          else:
              return guess


def user_guess(magic_number):
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

        elif my_guess > magic_number:
            print("--------- *TOO HIGH!!* ---------\n")
            attempts += 1

        else:

            print("""
    ===============================================
            GOOD JOB IT WAS:\n 
            {} 
            YOU GUESSED:\n 
            {}
            WITH {} TRIES
    ===============================================""".format(magic_number, my_guess, attempts))

def number_gen():
    '''
    - Create a Random Generated Number between 1 - 8

    '''
    magic_number = random.randint(1, 8)
    if magic_number == 0:
        magic_number += 1
    return magic_number

# print a welcome to the user on game start
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
        print("Please Enter 'Yes' or 'No':\n  " )

def game_start():
    '''
    STEPS:
    * * ATTENTION * * READ ME
    1 - welcome the user    √ DONE
    2 - Generate a number
    3 - ASK For a number and store it
    '''
    # STEP 1


your_score = 0
attempts = 0
number = number_gen()

while True:
     tries = user_guess(number)
     your_score = attempts
     print_welcome()









    


if __name__ == '__main__':
    game_start()

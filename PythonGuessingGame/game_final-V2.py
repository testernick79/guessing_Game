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



def number_gen():
    '''
    - Create a Random Generated Number

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

def main():
    '''
    STEPS:
    * * ATTENTION * * READ ME
    1 - welcome the user
    2 - Generate a number
    3 - ASK For a number and store it
    '''
    # STEP 1
    is_playing = True
    return print_welcome()

        








        
    
        




if __name__ == '__main__':
    main()

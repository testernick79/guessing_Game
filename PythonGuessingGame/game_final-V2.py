import random

'''- prompt the user for a number, Handle invalid values
   - Store a message, return a stored value entered'''
def useNumbers(message = "Pick a Number:    "):
    while True:
        try:
            user_answer = int(input(message))
            return user_answer
        except ValueError:
            print("You must enter a number, Try Again!: ")

'''
    - create a random number variable
'''
def randomNumber():
    magic_number = random.randint(1, 8)
    return magic_number

'''- Checks the users number
   - Prints users answer and generated number if the guess is correct
   '''
def checkUserNumbers(user_answer, magic_number):
    if user_answer > magic_number:
     print("---------------------TOO LOW!---------------------")
    elif user_answer < magic_number:
        print("---------------------TOO HIGH!---------------------")
    else:
        print(" Great Guess the answer {} and you choose {}".format(user_answer, magic_number))

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

def play_again():
    try_again = input(" Do you want to play again Y/N:?    \n").lower()

    if try_again in ['y', 'yes']:
        return True

    elif try_again in ['n', 'no']:
        return False

    else:
        print_come_back()

def main():
    '''
    STEPS:
    * * ATTENTION * * READ ME
    1 - welcome the user
    2 - Generate a number
    3 - ASK For a number and store it
    '''
    is_playing = True
    return print_welcome()
    
        




if __name__ == '__main__':
    main()

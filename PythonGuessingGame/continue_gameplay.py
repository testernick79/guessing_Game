def print_welcome_message(): #------------DONE------------
    """Prints the welcome message to the user"""
    print("Welcome to the age game")#------------DONE------------

def get_users_age():#------------DONE------------
    """
    Gets the user's age from the user

    :return: Integer of the user's age
    """
    while True:#------------DONE------------
        try:#------------DONE------------
            age = int(input("What is your age?      "))#------------DONE------------
        except ValueError:#------------DONE------------
                print("Please enter an integer like 5\n     ")#------------DONE------------
        else:#------------DONE------------
            return age#------------DONE------------

def play_again():#------------DONE------------
    """
    Asks the user if they want to play again

    :return: Boolean
    """

    while True:#------------DONE------------
        try_again = input("Do you want to play again?")#------------DONE------------

        if try_again in ['y', 'yes', 'absolutly']:#------------DONE------------
            return True#------------DONE------------
        elif try_again in ['n', 'no', 'never']:#------------DONE------------
            return False#------------DONE------------
        else:#------------DONE------------
            print("Please enter 'yes' or 'no'.\n")#------------DONE------------

def run_game():#------------DONE------------
    """
    This is the main game loop, which continues the game until the user ends it
    """
    continue_game = True#------------DONE------------
    print_welcome_message()#------------DONE------------

    while continue_game:#------------DONE------------
        age = get_users_age()

        # Customize the user's age message
        if age < 23:
            print("Make sure to enjoy your teen years!\n")
        else:
            print("Don't think to much about your past. The future awaits!\n")

        continue_game = play_again()


if __name__ == __name__:
    run_game()

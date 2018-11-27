"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():

    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.


if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
    print("---------------------Welcome to the game!---------------------")
    lucky_Number = random.randrange(1,22)
    print("Let's Play a Game! I'm thinking of a number between 1-22! You have 5 chances")
guessed_Number = False
    
while guessed_Number == False:
    userInput = int(input("Make a Guess?"))
    
    # this statement runs first...
	# if its True, the other elifs dont run.
    if userInput == lucky_Number:
        guessed_Number = True
        print(str(lucky_Number) +  " Great Guess! You Got it")
        
    
    # this elif only runs, if the `if` above was False.    
    elif userInput > lucky_Number:
        print(" is too high, try again!")
        
    
    # this elif only runs, if the `elif` above was False.    
    elif userInput < lucky_Number:
        print(" is too low, try again!")
        
    
    # this elif only runs, if the `elif` above was False.    
    elif userInput > 5:
        print(" Your Wrong!" + "Was the correct answer")
        break
        
print("---------------------GAME OVER---------------------")

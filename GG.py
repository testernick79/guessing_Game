# Python Number Guessing GAME
#REQUIREMENTS

#If they choose correctly display they got it, and tell them the number guessed and the number it was as well as how many tries
# After the game is done the user can enter a new game. 
# a new randome number is generated.
# limit the number of tries to 5
import random

#Generate a random number from 1,20
def randomNumber():
  magic_number = random.randint( 1, 20 )

#Any user can return and use the Magic number returned  
  return magic_number

#Prompt the user to ask for the number they want to choose
def userNumbers(text_message = "Pick a Number: " ):
  user_answer = (input( text_message ))
  
  #Any user can return and use the user answer returned
  return user_answer

#If the number is too high, tell them  it is too high and try again
#If the number is too low, tell them  it is too low and try again
def checkUserNumber( user_answer, magic_number ):
  if user_answer > magic_number:
    return "too high , try again"
  elif user_answer < magic_number:
    return "too low , try again"
  else: "Great Guess! you chose user_answer, and the correct answer was magic_number, with only tries!"
    
# Start the game
def main():
  user_success = False
  start_game = True
  
  #if either are true game will run
  while user_success or start_game:
    
    user_answer = userNumbers()
    magic_number = randomNumber()
    numberChosen = userNumbers()
    text_message = checkUserNumber( user_Answer, randomNumber  )
  
  #display a message when the user guesses correct.
    while text_message != "Great Guess! you chose and the correct answer was/n with only magic_Number, tries!":
      print( text_message )
    
  #Change the message after the first time ran.  
    numberChosen = userNumbers( "Please Try Again!: " )
    text_message = user_answer( user_answer, randomNumber )
    
    print( text_message )
    user_success = True
    
main()  
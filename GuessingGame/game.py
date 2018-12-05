
import random
print("---------------------Welcome to the game!---------------------")
print("Let's Play a Game!") 
print("I'm thinking of a number between 1-22! You have 3 chances")

input("\nPress enter to Start")
def start_game():


  if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()

# Define values
player = int(input(" What's Your Guess? "))
lucky_Number = random.randrange(1,22)
count = 0    

while player != lucky_Number:
  
  if  player > lucky_Number:
    print("------------------* *Too HIGH! Try Again* *------------------ ")
    
  elif player < lucky_Number:
    print("------------------* *Too LOW! Try Again* *------------------ ")
    
    player=int(input("What's Your Guess? "))
    count += 1
    if count == 3:
      break
      
print("Great Guess! I was thinking: {} and you guessed: {} You tried {} times".format(lucky_Number, player, count))
    
        
print("\n ------------------* *GAME OVER* *------------------ ")
input("\nPress enter to exit")

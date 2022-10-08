# SNAKE WATER GUN GAME : 
import random
def game(computer , player_input):
    # If two values are equal , declare a tie!
    if computer == player_input:
        return None
    # Check for all possibilities when computer choose "s". 
    elif computer == "s":
        if player_input == "w":
            return False
        elif player_input == "g":
            return True
    # Check for all possibilities when computer choose "w". 
    elif computer == "w":
        if player_input == "g":
            return False
        elif player_input == "s":
            return True
    # Check for all possibilities when computer choose "g". 
    elif computer == "g":
        if player_input == "w":
            return True
        elif player_input == "s":
            return False
random_number = random.randint(1 , 3)   
if random_number == 1:
    computer = "s"
elif random_number == 2:
    computer = "w"
else:
    computer = "g"
player_input = input('''Your Turn =>
Choose any one of the following:
s : Sanke(s)
w : Water(w) 
g : Gun(g) \n''')
a = game(computer , player_input)
print(f"Computer choosed : {computer}")
print(f"You Choose : {player_input} ")
if a == None:
    print("The game is tie!")
elif a == True:
    print("You Win!")
else:
    print("You Loose!")
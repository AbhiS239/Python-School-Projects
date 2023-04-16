# Importing the nessecary libraries
import random

# Initialize an empty list to hold the names of players 
myList = [] 

## Define the gameround() function
def gameRound(myList, listLength, Werewolf, Healer, nightNum):
    '''
    Args:
        myList (list): A list of player names
        listLength (int): How many players there will be
        Werewolf (str): The name of the Werewolf
        Healer (str): The name of the Healer
        nightNum (int): How many nights have passed
    '''
# Chooses a random player to be the Victim
    Victim = random.choice(myList)
    # Chooses a random player to be protected 
    Protected = random.choice(myList)
    # If the victim is the Werewolf, begin another round 
    if Victim == Werewolf:
        gameRound(myList, listLength, Werewolf, Healer, nightNum)
    # If the Victim is protected and the Healer is still alive, protect the Victim 
    elif Victim == Protected and Healer in myList:
        print(f'On Night {nightNum}, {Victim} was protected by The Healer\n')
        print(myList)
    # If the Victim is the Healer, announce that the Healer has been killed and remove from the list
    elif  Victim == Healer:
        print(f'On Night {nightNum}, The Healer has been taken out. {Victim} was The Healer, The Village no longer has a Healer\n')
        myList.remove(Healer)
        print(myList)
    # If the Werewolf selects a Victim without any protection, it eliminates them are removes from the list 
    else:
        print(f'On Night {nightNum}, {Victim} was taken out by The Werewolf\n')
        myList.remove(Victim)
        print(myList)

# Keeps track of how many nights have occured 
nightNum = 0
def nightCount():
    '''
    Uses the nightNum global variable and adds one after every gameround() has occured
    '''
    global nightNum
    nightNum += 1  

while True:
# Ask the user how many players there will be
    listLength = int(input("How Many Players Will There Be?: "))
    if listLength <= 0:
        print("How are you gonna play the game bro?")
    break

# Prompt the user to enter the names of the players
for i in range(listLength):
    Villager = input("Name A Villager: ")
    if Villager == '':
        print("Well you just wasted a spot, you must input a name.")
    elif Villager == 'done':
        break
    else:
        Villager
        myList.append(Villager)
# Print the list of players 
print(myList)   

# Choose a random player to be the Werewolf
Werewolf = random.choice(myList)

# Choose a random player to be the Healer 
Healer = random.choice(myList)

# As long as the werewolf is equal to the healer, keep doing this over and over again until it's not anymore
while Werewolf == Healer:
    Werewolf = random.choice(myList)
    Healer = random.choice(myList)

while True:
    nightCount()
    gameRound(myList, listLength, Werewolf, Healer, nightNum)
    # If there are only 2 people left in the list and they both are Werewolf and Healer the game won't end so print that statement 
    if len(myList) == 2 and Werewolf and Healer in myList:
        print("This game will never end, it's just the healer and werewolf left")
        break
    # If the Werewolf is the only one left in the list, the game is over and you have lost and break out of loop
    if len(myList) == 1:
        print(f'How did you not guess the Werewolf? It was {myList[0]}. There is no one left in this village anymore.')
        break
    # Prompt the user to guess who the Werewolf is 
    Guess = input('Who do you think The Warewolf is?: ')
    # If the guess is the werewolf you have won the game 
    if Guess == Werewolf:
        print(f'On Night {nightNum}, The Werewolf has been caught. {Guess} was The Werewolf. Good Game\n')
        break
    # If the guess isn't even in the list, it's a wasted turn
    if Guess not in myList:
        print(f'{Guess} is not an option dawg, you just wasted a turn\n')
    # If everything is normal and the guess is incorrect just print the normal statement
    else: 
        print(f'{Guess} is not The Warewolf\n')


import random #Importing library to generate random numbers; implementing the game of chance aspect of the code
import time #Importing library to implement a set pace for the game
from collections import Counter #Importing collections.Counter library for Counter data structure

#Define themes, symbols, and betting options. Implementing through an immutable array
themes = {
    "Classic": (" 7", "🍊", "🍒", "🍀"),
    "Fruit": (" 7", "🍋", "🍇", "🍉"),
    "Animal": (" 7", "🐱", "🐭", "🐹"),
    "Aquarium": ("7", "🐠", "🐡", "🦈"),
    "Vehicles": ("7", "🚗", "🏍️", "🏎️")
}

#Initializing and tracking variables

freespinwin = 0 #Winnings from free spins
initialcredits = 100 #Player's credits
current_level = 1 #Player's current level/account status
winround = 0 #Number of rounds won
totalround = 0 #Number of rounds played
winningcondition = None
itemlist = None
selectedtheme = None

credit = initialcredits #Current value of credits availiable to gamble
winnings = {} #Creating an empty dictionary in order to store wins within each round
level_wins = Counter() #Utilizing Counter to keep track of wins per level
bonus_wins = Counter() #Utilizing Counter to keep track of bonus wins
jackpot_wins = Counter() #Utilizing Counter to keep track of jackpot wins


wins_to_unlock_hearts = {  #Defining the win requirments needed to unlock hearts for each level
    1: 2,   #Level 1 = 2 wins
    2: 3,   #Level 2 = 3 aditional wins
    3: 4,   #Level 3 = 4 aditional wins
    4: 5,   #Level 4 = 5 aditional wins
}

level_hearts = { #add my detailed comment #FIX AND ADD HEARTS
    1: None,
    2: None,
    3: None,
    4: None
}

class Queue: #Creating a queue data structure (class queue)
    """
    Class of queue for round's history
    """
    def __init__(self,size): #Establishing requirements for queue
        """
        Define the requirement for queue and creating list to store the history

        """
        self.size = size     #Establishing the max size of the queue
        self.historylist=[]  #Creating a list to store history

    def enqueue(self, item):  #Function to keep the history updated
        """
        Function to update the list of history
        if data in list more than 5, delete oldest data and add newest data
        """
        if len(self.historylist) >=self.size: #If number of data in the list more than 5
            self.historylist.pop(0)  #Delete oldest data
            self.historylist.append(item) #Add latest data

    def get_history(self):  #Function print data; presenting history
        """
        Function to presenting history

        """
        return self.historylist  #Display data in list

slothistory = Queue(5) #Create queue for storing last 5 rounds history

def addspinhistory(bet_amount, win_amount, symbols): #Function to add spin data into the list
    """
    Add spin data each round into the list of spin's history
    """
    spindata = {
        "Bet amount": bet_amount,  #Store bet data
        "Win amount": win_amount,  #Store win amount
        "Symbols": symbols         #Store generated symbols
    }
    slothistory.enqueue(spindata) #Updating history

def calwinrate(history): #Function to calculate winrate
    """
    Function to calculate user's winrate
    """
    if totalround !=0: #Check if totalround have data
        winrate = (winround/totalround) * 100 #Calculating winrate
    else:
        winrate = 0  #Error handling, for if no rounds have been played
    return winround, winrate  #Return calculations

def displayhistory(history):                    #Function to show history of rounds and win rate
    """
    Function to display user's history and user's stats
    """
    totalwin, winrate= calwinrate(history)      #Calculating totalwin and winrate
    print("\nRound history and Win rate: ")     #Print statements / visual formating
    print("Total Round Played: ", totalround)
    print("Total Wins: ", totalwin)
    print(f"All-Times Win Rates: {winrate:.2f} %")
    print(
        "**Please note that free spins are not recorded in the history and are not involved in win rate calculations.**")
    print("----------------------------------------------")
    time.sleep(1.5)

    print("\nLast 5 Rounds History: ")     #Print text / visual formating
    i = 1                                  #Initializimg roundnumber Counter
    history = slothistory.get_history()    #Pulling history from previous 5 round
    for round_info in history:             #Loop over print history
        print(f"{i}. {round_info}")        #Print round number information
        i += 1                             #Update variable value
        if round_info['Bet amount'] ==0:   #Adding to noted that it's trial round
            print("--trial round--")


#Implementing A Tree Data Structure
class TreeNode: #Creating class to hold tree node
    """
    Class of treenode
    """
    def __init__(self, level, heart): #Composing TreeNode class
        self.level = level            #Setting level of node
        self.heart = heart            #Setting heart symbol of node
        self.left = None              #Setting left child of node
        self.right = None             #Setting right child of node

def create_tree(current_level, level_hearts):                                 #Creating a function to configure a tree based on the user's current level and unlocking hearts
    """
    Function to configure a tree based on user's current level and unlocking heart
    :param current_level: User's current level
    :param level_hearts: User's current heart
    :return:
    """
    root = TreeNode(1, level_hearts.get(1, "🖤"))                       #Establishing the root node with level 1 and assigned heart
    if current_level >= 2:                                                    #Assigning notes based on user level and calling for the corriponding hearts
        root.left = TreeNode(2, level_hearts.get(2, "🖤🖤"))            #Left child
    if current_level >= 3:
        root.right = TreeNode(3, level_hearts.get(3, "🖤🖤🖤"))         #Right child
    if current_level == 4:
        root.left.left = TreeNode(4, level_hearts.get(4, "🖤🖤🖤🖤"))   #Left grandchild
    return root

def display_tree(node):                             #Displaying tree node
    """
    Function of displaying tree node
    :param node: Tree node
    :return:
    """
    if node is not None:                            #Checking the node isn't empty
        display_tree(node.left)                     #Recursivly having the left subtree displayed (---------------------maybe_change--------------)
        print(f"Level {node.level}: {node.heart}")  #Displaying the hearts of the current node
        display_tree(node.right)                    #Displaying text with same purpose of display_tree(node.left)

def unlock_hearts(current_level):                                                                                      #Unlcoking hearts based off of win requirements
    """
    Function to unlocking hearts based off winning requirement
    :param current_level: User's current level
    :return:
    """
    wins_required = wins_to_unlock_hearts[current_level]                                                               #Collecting the required wins for level up
    if level_wins[current_level] >= wins_required and level_hearts[current_level] is None:                             #Checkinng eligibility
        level_hearts[current_level] = "🖤" * current_level                                                             #Unlocking corrisponding heart symbol
        print(f"Congratulations! You've unlocked the heart for level {current_level}: {level_hearts[current_level]}")  #Displying achievement


#NOTE: REVISE JACKPOT & BONUS TO APPLY TO ALL THEMES
def search_for_winning_jackpot(firstsq, secondsq, thirdsq, fourthsq):
    """
    Function of searching for winning jackpot
    :param firstsq: First slot's symbol in the game
    :param secondsq: Second slot's symbol in the game
    :param thirdsq: Third slot's symbol in the game
    :param fourthsq: Fourth slot's symbol in the game
    :return:
    """
    jackpot_items= ("🍀", " 7")                                                             #Defining the winning items
    if all(symbol in jackpot_items for symbol in [firstsq, secondsq, thirdsq, fourthsq]):   #Defining the winning combinations and checking if present
        jackpot_wins["jackpot"] += 1                                                        #Prograssing user through Jackpot journey
        if jackpot_wins["jackpot"] == 5:                                                    #Checking if cobiniation has been met 5 times
            return True                                                                     #Provide update to jackpot progress
    return False                                                                            #Identifing there is no jackpot update

#Same application used for jackpot but cobination needs to be met twice rather than five times
def search_for_winning_bonus (firstsq, secondsq, thirdsq, fourthsq):
    """
    Function to define the winning bonus
    :param firstsq: First slot's symbol in the game
    :param secondsq: Second slot's symbol in the game
    :param thirdsq: Third slot's symbol in the game
    :param fourthsq: Fourth slot's symbol in the game
    :return:
    """
    bonus_items= ("🍀", " 7")
    if all(symbol in bonus_items for symbol in [firstsq, secondsq, thirdsq, fourthsq]):
        bonus_wins["bonus"] += 1
        if bonus_wins["bonus"] == 2:  #2 "🍀", " 7" combinations to win
            return True
    return False

class MysteryTheme(TreeNode): #class for mysterytheme
    """
    Class of mystery theme by using tree node
    """
    def __init__(self, level, heart, theme):
        """
        Function to initialise new treenode object
        :param level: level of tree node
        :param heart: heart represent treenode
        :param theme: theme of treenode
        """
        super().__init__(level, heart)
        self.theme = theme

def create_tree(current_level, level_hearts):
    """
    Function to create tree for mystery tree
    :param current_level: User's current level
    :param level_hearts: User's current heart level
    :return:
    """
    root = TreeNode(1, level_hearts.get(1,"🖤"))
    if current_level >= 2:
        root.left = TreeNode(2, level_hearts.get(2, "🖤🖤"))  # Left child for level 2
        if current_level == 2:
            print("You've reached level 2 and unlocked the 'Aquarium' theme!")
            time.sleep(1)
    if current_level >= 3:
        root.right = TreeNode(3, level_hearts.get(3, "🖤🖤🖤"))  # Right child for level 3
        if current_level == 3:
            print("You've reached level 3 and unlocked the 'Vehicles' theme!")
            time.sleep(1)
    if current_level == 4:
        root.left = TreeNode(4, level_hearts.get(4, "🖤🖤🖤🖤"))  # Left grandchild for level 4
    return root

def print_slot_result(firstsq, secondsq, thirdsq, fourthsq):
    """
    Print the result of the slot machine spin with symbols displayed horizontally.

    Parameters:
        firstsq (str): Symbol for the first slot.
        secondsq (str): Symbol for the second slot.
        thirdsq (str): Symbol for the third slot.
        fourthsq (str): Symbol for the fourth slot.
    """
    print("| ", random.choice(itemlist), " | ", random.choice(itemlist), " | ", random.choice(itemlist),
          " | ", random.choice(itemlist), " | ")
    print('------------------------------')
    print("| ", firstsq, " | ", secondsq, " | ", thirdsq, " | ", fourthsq, " |")
    print('------------------------------')
    print("| ", random.choice(itemlist), " | ", random.choice(itemlist), " | ", random.choice(itemlist),
          " | ", random.choice(itemlist), " | ")
    print('------------------------------')

# Function to allow players to choose theme, symbols, and betting options
def choose_options():
    """
    Function to choosing theme's option
    :return:xdd
    """
    print("Welcome to the Slot Machine. Please select a theme:"
          "\n1 -- Classic,", themes["Classic"],
          "\n2 -- Fruit", themes["Fruit"],
          "\n3 -- Animal", themes["Animal"])
    if current_level >= 2: #if current level more than 2
        print("4 -- Aquarium", themes["Aquarium"]) #show mystery theme
    if current_level >= 3: #if current level more than 3
        print("5 -- Vehicles", themes["Vehicles"]) #show mystery theme
    if current_level == 1:
        selectedtheme = input("Please choose a number between 1 and 3: ") #asking for choosing the theme
        if selectedtheme not in ['1', '2', '3']: #if user put something not from 1,2, 3
            print("Invalid selection, please try again.")
            time.sleep(1)
            print("")
            return choose_options() #go back and ask again
    if current_level == 2:
        selectedtheme = input("Please choose a number between 1 and 4: ") #asking for choosing the theme
        if selectedtheme not in ['1', '2', '3','4']: #if user put something not from 1,2, 3
            print("Invalid selection, please try again.")
            time.sleep(1)
            print("")
            return choose_options() #go back and ask again
    if current_level >= 3:
        selectedtheme = input("Please choose a number between 1 and 5: ") #asking for choosing the theme
        if selectedtheme not in ['1', '2', '3','4','5']: #if user put something not from 1,2, 3
            print("Invalid selection, please try again.")
            time.sleep(1)
            print("")
            return choose_options() #go back and ask again

    if selectedtheme =='1': #if typing '1'
        itemlist = themes["Classic"] #select itemlist classic
        winningcondition = (
        "\n1. Earn £30000. You will start with £100 and gain more based off achieving the following winning combinations:"
        "\n\t\t🍒\t\t\t\t\t🍒\t\t\t\t\t🍒\t\t\t\t\t🍒\t\t\tWinning amount:\tBet amount *20"
        "\n\t  7/🍊/🍀\t\t\t  7/🍊/🍀\t\t\t  7/🍊/🍀\t\t\t  7/🍊/🍀\t\tWinning amount:\tBet amount *5"
        "\n\t\t🍊\t\t\t\t\t🍊\t\t\t\t   🍒/🍊\t\t\t  ______\t\tWinning amount:\tBet amount *3"
        "\n\t\t7\t\t\t\t\t7\t\t\t\t  ______\t\t\t  ______\t\tWinning amount:\tBet amount *2"
        "\n\t7/🍊/🍒/🍀\t\t\t  ______\t\t\t7/🍊/🍒/🍀\t\t\t  ______\t\tWinning amount:\tBet amount *2"
        "\n\t  ______\t\t\t7/🍊/🍒/🍀\t\t\t  ______\t\t\t7/🍊/🍒/🍀\t\tWinning amount:\tBet amount *2"
        "\n\t7/🍊/🍒/🍀\t\t\t  ______\t\t\t  ______\t\t\t7/🍊/🍒/🍀\t\tWinning amount:\tFree spin")

    elif selectedtheme =='2': #if typing '2'
        itemlist = themes["Fruit"] #select itemlist fruit
        winningcondition = (
            "\n1. Earn £30000. You will start with £100 and gain more based off achieving the following winning combinations:"
            "\n\t\t🍉\t\t\t\t\t🍉\t\t\t\t\t🍉\t\t\t\t\t🍉\t\t\tWinning amount:\tBet amount *20"
            "\n\t   7/🍇/🍋\t\t\t   7/🍇/🍋\t\t\t   7/🍇/🍋\t\t\t   7/🍇/🍋\t\tWinning amount:\tBet amount *5"
            "\n\t\t🍇\t\t\t\t\t🍇\t\t\t\t   🍉/🍇\t\t\t  ______\t\tWinning amount:\tBet amount *3"
            "\n\t\t 7\t\t\t\t\t 7\t\t\t\t  ______\t\t\t  ______\t\tWinning amount:\tBet amount *2"
            "\n\t 7/🍇/🍉/🍋\t\t  ______\t\t\t 7/🍇/🍉/🍋\t\t  ______\t\tWinning amount:\tBet amount *2"
            "\n\t  ______\t\t\t 7/🍇/🍉/🍋\t\t  ______\t\t\t 7/🍇/🍉/🍋\tWinning amount:\tBet amount *2"
            "\n\t 7/🍇/🍉/🍋\t\t  ______\t\t\t  ______\t\t\t 7/🍇/🍉/🍋\tWinning amount:\tFree spin")

    elif selectedtheme =='3': #if typing '3'
        itemlist = themes["Animal"] #select itemlist animal
        winningcondition = (
            "\n1. Earn £30000. You will start with £100 and gain more based off achieving the following winning combinations:"
            "\n\t\t🐱\t\t\t\t\t🐱\t\t\t\t\t🐱\t\t\t\t\t🐱\t\t\tWinning amount:\tBet amount *20"
            "\n\t   7/🐭/🐹\t\t\t   7/🐭/🐹\t\t\t   7/🐭/🐹\t\t\t   7/🐭/🐹\t\tWinning amount:\tBet amount *5"
            "\n\t\t🐭\t\t\t\t\t🐭\t\t\t\t   🐱/🐭\t\t\t  ______\t\tWinning amount:\tBet amount *3"
            "\n\t\t 7\t\t\t\t\t 7\t\t\t\t  ______\t\t\t  ______\t\tWinning amount:\tBet amount *2"
            "\n\t 7/🐭/🐱/🐹\t\t  ______\t\t\t 7/🐭/🐱/🐹\t\t  ______\t\tWinning amount:\tBet amount *2"
            "\n\t  ______\t\t\t 7/🐭/🐱/🐹\t\t  ______\t\t\t 7/🐭/🐱/🐹\tWinning amount:\tBet amount *2"
            "\n\t 7/🐭/🐱/🐹\t\t  ______\t\t\t  ______\t\t\t 7/🐭/🐱/🐹\tWinning amount:\tFree spin")

    elif selectedtheme == '4' and current_level >= 2:  # if typing '4'
        itemlist = themes["Aquarium"]  # select itemlist Aquarium
        winningcondition = (
            "\n1. Earn £30000. You will start with £100 and gain more based off achieving the following winning combinations:"
            "\n\t\t🦈\t\t\t\t\t🦈\t\t\t\t\t🦈\t\t\t\t\t🦈\t\t\tWinning amount:\tBet amount *30"
            "\n\t   7/🐠/🐡\t\t\t   7/🐠/🐡\t\t\t   7/🐠/🐡\t\t\t   7/🐠/🐡\t\tWinning amount:\tBet amount *7.5"
            "\n\t\t🐠\t\t\t\t\t🐠\t\t\t\t   🦈/🐠\t\t\t  ______\t\tWinning amount:\tBet amount *4.5"
            "\n\t\t 7\t\t\t\t\t 7\t\t\t\t  ______\t\t\t  ______\t\tWinning amount:\tBet amount *3"
            "\n\t 7/🐠/🦈/🐡\t\t  ______\t\t\t 7/🐠/🦈/🐡\t\t  ______\t\tWinning amount:\tBet amount *3"
            "\n\t  ______\t\t\t 7/🐠/🦈/🐡\t\t  ______\t\t\t 7/🐠/🦈/🐡\tWinning amount:\tBet amount *3"
            "\n\t 7/🐠/🦈/🐡\t\t  ______\t\t\t  ______\t\t\t 7/🐠/🦈/🐡\tWinning amount:\tFree spin"
            "The Mystery Theme awards 1.5 times rewards.")

    elif selectedtheme == '5' and current_level >= 3:  # if typing '5'
        itemlist = themes["Vehicles"]  # select itemlist Vehicles
        winningcondition = (
            "\n1. Earn £30000. You will start with £100 and gain more based off achieving the following winning combinations:"
            "\n\t\t🏎\t\t\t\t\t🏎\t\t\t\t\t🏎\t\t\t\t\t🏎\t\t\tWinning amount:\tBet amount *40"
            "\n\t   7/🚗/🏍\t\t\t   7/🚗/🏍\t\t\t   7/🚗/🏍\t\t\t   7/🚗/🏍\t\tWinning amount:\tBet amount *10"
            "\n\t\t🚗\t\t\t\t\t🚗\t\t\t\t   🏎/🚗\t\t\t  ______\t\tWinning amount:\tBet amount *6"
            "\n\t\t 7\t\t\t\t\t 7\t\t\t\t  ______\t\t\t  ______\t\tWinning amount:\tBet amount *4"
            "\n\t 7/🚗/🏎/🏍\t\t\t  ______\t\t\t 7/🚗/🏎/🏍\t\t\t  ______\t\tWinning amount:\tBet amount *4"
            "\n\t  ______\t\t\t 7/🚗/🏎/🏍\t\t\t  ______\t\t\t 7/🚗/🏎/🏍\t\tWinning amount:\tBet amount *4"
            "\n\t 7/🚗/🏎/🏍\t\t\t  ______\t\t\t  ______\t\t\t 7/🚗/🏎/🏍\t\tWinning amount:\tFree spin"
            "--The Mystery Theme awards double rewards.--")

        print()

    print("")
    print("                               ꧁  𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐭𝐡𝐞 𝐂𝐃𝐆 𝐒𝐥𝐨𝐭 𝐌𝐚𝐜𝐡𝐢𝐧𝐞  ꧂")  # the welcome message
    print("")
    print(
        "        \033[1mTo beat the game you must have more than £30000\033[1m")  # using ANSI escape sequences to bold text
    time.sleep(1)
    print("")
    print("itemlist: ", itemlist)
    print(winningcondition)
    time.sleep(2)
    print(
        "\n2. Pass all four levels of status: \n\t2 wins \t\tlevel 1\t\t🖤 \n\t3 wins \t\tlevel 2\t\t🖤🖤 \n\t4 wins \t\tlevel 3\t\t🖤🖤🖤 \n\t5 wins \t\tlevel 4\t\t🖤🖤🖤🖤")
    print("")
    print("LET THE GAMES BEGIN...")
    return selectedtheme, itemlist


firstsq = None #variable for first slot
secondsq = None #variable for second slot
thirdsq = None #variable for third slot
fourthsq = None #variable for fourth slot

while True: #Create loop
    #add detailed comment
    try:
        selectedtheme, itemlist = choose_options()
        player_tree = create_tree(current_level, level_hearts)
        display_tree(player_tree)

        while credit > 0: #While user still have credits
            print("\033[1m\nAccount Balance:","£",credit) #\nAccount Status:", level_hearts[current_level], "\033[1m") #printing and updating the account information

            try:
                bet_amount_input = input("\n\tOptions:"
                                     "\n\tType 'trial' for free trial"
                                     "\n\tType 'history' to see your last 5 round history and all-time winrate, "
                                     "\n\tType 'quit' to exit the game."
                                     "\n\tType 'theme to choose a different themes"
                                     "\n\n\tEnter Bet Amount or Select Listed Option: ") #Asking how much user want to place a bet, if user want to try the spin type'0', want to exit program type 'quit'
            except KeyboardInterrupt:
                print("\nYou've interrupted the program. Please start over.") #For when the user interupts the program by terminating the terminal mid response
                break

            if bet_amount_input.lower() == "trial": #change user input to lowercase and if input 'trial'
                bet_amount = 0 #given bet amount =0 and start free trial round

            elif bet_amount_input.lower() == "quit": #change user input into lowercase and if input == 'quit'
                break #break the loop

            elif bet_amount_input.lower() == "history":  #change user input into lowercase and if input == 'history'
               if slothistory.get_history(): #checkk if history empty or not
                    displayhistory(slothistory.get_history()) #call function to print history and winrate
                    time.sleep(1.5)
               else:
                   print("\nNo history available yet.")
               continue #restart the loop

            elif bet_amount_input.isdigit(): #if user input is in degit
                bet_amount = int(bet_amount_input) #change user input into integer format
                if bet_amount ==0: #check if bet amount is equal to '0'
                    print("invalid input, Please enter a positive integer for the bet amount.")
                    continue
                if bet_amount > credit: #check if bet amount is higher than user's credits
                    print("Not enough credit, please try again.") #show error message
                    continue #go back to start

            elif bet_amount_input.lower() == "theme": #if user input is theme
                selectedtheme, itemlist = choose_options() #choose new theme and update item
                continue
            else:
                print("Invalid input, please try again.")  # show error message  /  error handling
                continue

            if bet_amount >0:
                totalround+=1 #count totalround that have been played

            credit -= bet_amount  # update credits balance after putting the bet
            firstsq = random.choice(itemlist)  # random first symbol using the random function
            secondsq = random.choice(itemlist)  # random second symbol using the random function
            thirdsq = random.choice(itemlist)  # random third symbol using the random function
            fourthsq = random.choice(itemlist)  # random fourth symbol using the random function
            print("Stake accepted. Good luck.")
            print("Spinning now...")
            time.sleep(1)  # delay the program for 1 second
            #Display Slot result
            print_slot_result(firstsq,secondsq,thirdsq,fourthsq)
            # adding different ways to win
            bet_win = 0
            if firstsq == secondsq == thirdsq == fourthsq and [firstsq,secondsq,thirdsq,fourthsq] != ['🍒', '🍉', '🐱','🦈','🏎']:
                bet_win = bet_amount * 5
            elif firstsq == secondsq == thirdsq == fourthsq in ['🍒', '🍉', '🐱','🦈','🏎']:
                bet_win = bet_amount * 20
            elif firstsq == thirdsq:
                bet_win = bet_amount * 2
            elif secondsq == fourthsq:
                bet_win = bet_amount * 2
            elif (firstsq == secondsq == '🍊' or firstsq == secondsq == "🍇" or firstsq == secondsq == '🐭' or firstsq == secondsq == '🐠' or firstsq == secondsq == '🚗') and (thirdsq in ['🍊', '🍇', '🐭', '🍒', '🍉', '🐱','🐠','🦈','🏎','🚗']):
                bet_win = bet_amount * 3
            elif (firstsq == secondsq) and (firstsq in ['7', ' 7', ' 7']):
                bet_win = bet_amount * 2


            if bet_win > 0:
                if selectedtheme == "4":
                    bet_win *=1.5
                if selectedtheme == "5":
                    bet_win *=2
                print("You won £", bet_win)
                credit += bet_win
                winnings[len(winnings) + 1] = bet_win
                winround +=1 #round win count


            # free spins
            if firstsq == fourthsq:
                free_spins = random.randint(1,5) # win bet 1 and 5 free spins
                print(f'you won {free_spins} free spins')

                freespinwin = 0 # initializing the freespinwin variable
                for i in range(free_spins):
                    print('you have a free spin')
                    firstsq = random.choice(itemlist)
                    secondsq = random.choice(itemlist)
                    thirdsq = random.choice(itemlist)
                    fourthsq = random.choice(itemlist)

                    print("Spinning now...")
                    time.sleep(1)

                    print_slot_result(firstsq,secondsq,thirdsq,fourthsq) #Display the slot game

                    #conditions to win free spins
                    spinwin = 0
                    if firstsq == secondsq == thirdsq == fourthsq:
                        spinwin = bet_amount * 5
                    elif firstsq == secondsq == thirdsq == fourthsq in ['🍒', '🍉', '🐱']:
                        spinwin = bet_amount * 20
                    elif firstsq == thirdsq:
                        spinwin = bet_amount * 2
                    elif secondsq == fourthsq:
                        spinwin = bet_amount * 2
                    elif (firstsq == secondsq == '🍊' or firstsq == secondsq == "🍇" or firstsq == secondsq == '🐭') and (
                            thirdsq in ['🍊', '🍇', '🐭', '🍒', '🍉', '🐱']):
                        spinwin = bet_amount * 3
                    elif (firstsq == secondsq) and (firstsq in ['7', ' 7', ' 7']):
                        spinwin = bet_amount * 2


                    freespinwin += spinwin # Accumulate the winnings from each free spin

                    if freespinwin > 0:
                        print("You won £", freespinwin)
                        credit += freespinwin
                        winnings[len(winnings) + 1] = freespinwin
                        level_wins[current_level] += 1
                    else:
                        print("You lost")

            #checking if the user beat the game
            if bet_win > 0 or freespinwin > 0:
                credit += bet_win
                level_wins[current_level] += 1
                unlock_hearts(current_level)
            else:
                print("You lost")

            #Checking if the current number of wins the bonus and adding the £500 award to the users overall credit
            if search_for_winning_jackpot(firstsq, secondsq, thirdsq, fourthsq):
                jackpot_money = 500  #Jackpot money of £500
                credit += jackpot_money  #Adding prize to credit
                print(f"Congratulations! You've spun the jackpot combination five times and won £{jackpot_money}!") #Informing user of jackpot acheivement


            #Checking if the current number of wins the bonus and adding the £200 award to the users overall credit
            if search_for_winning_bonus(firstsq, secondsq, thirdsq, fourthsq):
                bonus_money = 200  #Bonus money of £200
                credit += bonus_money  #Adding prize to credit
                print(f"Congratulations! You've spun the bonus combination twice and won £{bonus_money}!") #Informing user of bonus acheivement

            # Check if the user beat the game
            if credit >= 30000:
                print("Congratulations!, You have £", credit," You've beat the game!")
                time.sleep(1)
                break

            # Check if the current level requirement is met
            if current_level < 4 and level_wins[current_level] >= wins_to_unlock_hearts[current_level]:
                current_level += 1 #Progressing player to the next level
                player_tree = create_tree(current_level, level_hearts) #Forming a new player tree for the new level
                display_tree(player_tree) #Displying the updated tree

            #Updating spin history with current data
            addspinhistory(bet_amount,bet_win, [firstsq,secondsq,thirdsq,fourthsq])

    #Error handling incase user exits the gane while program awaits user input
    except Exception as e:
        print("Unfortunately, you've prompted an error:", str(e))
        print("Please try again.")

    #Farewell message
    print("Thank you for playing.")

    #Using Sort algorithm organize winnings in decinging order based on win amounts
    sorted_winnings = sorted(winnings.items(), key=lambda x: x[1], reverse=True)

    #Displaying the organized winnings
    print("\nWinnings sorted from highest to lowest:")
    for round_num, win_amount in sorted_winnings:
        print(f"Round {round_num}: £{win_amount}")

    #Ending user experience
    print("Exiting the game...") #Informing user the game is ending
    time.sleep(1.5) #Adding a delay beofre game ends
    break  #Exiting the game loop

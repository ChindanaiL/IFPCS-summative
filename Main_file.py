import random
import time
from collections import Counter, deque

# Define themes, symbols, and betting options
themes = {
    "Classic": [" 7","🍊","🍒","🍀"],
    "Fruit": ["🍏","🍋","🍇","🍉"],
    "Animal": ["🐶","🐱","🐭","🐹"]
}
#itemlist = [" 7","🍊","🍒","🍀"] #list of item in our slot machine, able to change it later
freespinwin = 0
initialcredits = 100 #initial player's credits
current_level = 1 #tracking the current level/account status
winround = 0
totalround = 0
credit = initialcredits
winnings = {}
bonus_wins = Counter()
level_wins = Counter()
jackpot_wins = Counter()


wins_to_unlock_hearts = {  #defining the win requirments needed to unlock hearts for each level
    1: 2,
    2: 3,
    3: 4,
    4: 5,
}

level_hearts = { #add my detailed comment
    1: None,
    2: None,
    3: None,
    4: None
}

class Queue: #Class queue
    def __init__(self,size):
        self.size = size
        self.historylist=[]
    def enqueue(self, item): #function to keep update the history
        if len(self.historylist) >=self.size: #if number of data in the list more than 5
            self.historylist.pop(0) #delete oldest data
        self.historylist.append(item) #add latest data
    def get_history(self): #function print data
        return self.historylist #display data in list

slothistory = Queue(5) #Create queue for storing last 5 rounds history

def addspinhistory(bet_amount, win_amount, symbols): #function to add spindata into the list
    spindata = {
        "Bet amount": bet_amount,
        "Win amount": win_amount,
        "Symbols": symbols
    }
    slothistory.enqueue(spindata)

def calwinrate(history): #function to calculate winrate
    if totalround !=0: #if totalround have data
        winrate = (winround/totalround) * 100 #find all time winrate
    else:
        0
    return winround, winrate

def displayhistory(history): #function to show history
    totalwin, winrate= calwinrate(history)
    print("\nRound history and Win rate: ")
    print("Total Round Played: ", totalround)
    print("Total Wins: ", totalwin)
    print(f"All-Times Win Rates: {winrate:.2f} %")
    print(
        "**Please note that free spins are not recorded in the history and are not involved in win rate calculations.**")
    print("----------------------------------------------")
    time.sleep(1.5)

    print("\nLast 5 Rounds History: ")  # print text
    i = 1
    history = slothistory.get_history()
    for round_info in history:  # loop print history
        print(f"{i}. {round_info}")
        i += 1


#add my detailed comment
class TreeNode:
    def __init__(self, level, heart):
        self.level = level
        self.heart = heart
        self.left = None
        self.right = None

# add my detailed comment
def create_tree(current_level, level_hearts):
    root = TreeNode(1, level_hearts.get(1, "🖤"))
    if current_level >= 2:
        root.left = TreeNode(2, level_hearts.get(2, "🖤🖤"))
    if current_level >= 3:
        root.right = TreeNode(3, level_hearts.get(3, "🖤🖤🖤"))
    if current_level == 4:
        root.left.left = TreeNode(4, level_hearts.get(4, "🖤🖤🖤🖤"))
    return root

# add my detailed comment
def display_tree(node):
    if node is not None:
        display_tree(node.left)
        print(f"Level {node.level}: {node.heart}")
        display_tree(node.right)

# add my detailed comment
def unlock_hearts(current_level):
    wins_required = wins_to_unlock_hearts[current_level]
    if level_wins[current_level] >= wins_required and level_hearts[current_level] is None:
        level_hearts[current_level] = "🖤" * current_level
        print(f"Congratulations! You've unlocked the heart for level {current_level}: {level_hearts[current_level]}")

# add my detailed comment
def search_for_winning_jackpot(firstsq, secondsq, thirdsq, fourthsq):
    jackpot_items= ("🍀", " 7")
    if all(symbol in jackpot_items for symbol in [firstsq, secondsq, thirdsq, fourthsq]):
        jackpot_wins["jackpot"] += 1
        if jackpot_wins["jackpot"] == 5:  #5 "🍀", " 7" combinations to win
            return True
    return False
def search_for_winning_bonus (firstsq, secondsq, thirdsq, fourthsq):
    bonus_items= ("🍀", " 7")
    if all(symbol in bonus_items for symbol in [firstsq, secondsq, thirdsq, fourthsq]):
        bonus_wins["bonus"] += 1
        if bonus_wins["bonus"] == 2:  #2 "🍀", " 7" combinations to win
            return True
    return False
# Function to allow players to choose theme, symbols, and betting options
def choose_options():
    print("Available Themes:")
    for theme in themes.keys():
        print(f"- {theme}")
    selected_theme = input("Choose a theme: ")

    if selected_theme not in themes:
        print("Invalid theme. Please choose from the available themes.")
        return choose_options()

    itemlist = themes[selected_theme]

    # Add more customization options here...

    return itemlist

print("")
print("                               ꧁  𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐭𝐡𝐞 𝐂𝐃𝐆 𝐒𝐥𝐨𝐭 𝐌𝐚𝐜𝐡𝐢𝐧𝐞  ꧂") #the welcome message
print("")
print("        \033[1mTo beat the game you must complete two main requirements and collect the diamond --> 💎\033[1m") #using ANSI escape sequences to bold text
print("")
#print("itemlist: ", itemlist)
print("\n1. Earn £500. You will start with £100 and gain more based off achieving the following winning combinations:"
      "\n\t\t🍒\t\t\t\t\t🍒\t\t\t\t\t🍒\t\t\t\t\t🍒\t\t\tWinning amount:\tBet amount *20"
      "\n\t  7/🍊/🍀\t\t\t  7/🍊/🍀\t\t\t  7/🍊/🍀\t\t\t  7/🍊/🍀\t\tWinning amount:\tBet amount *5"
      "\n\t\t🍊\t\t\t\t\t🍊\t\t\t\t   7/🍊\t\t\t\t  ______\t\tWinning amount:\tBet amount *3"
      "\n\t\t7\t\t\t\t\t7\t\t\t\t  ______\t\t\t  ______\t\tWinning amount:\tBet amount *2"
      "\n\t7/🍊/🍒/🍀\t\t\t  ______\t\t\t7/🍊/🍒/🍀\t\t\t  ______\t\tWinning amount:\tBet amount *2"
      "\n\t  ______\t\t\t7/🍊/🍒/🍀\t\t\t  ______\t\t\t7/🍊/🍒/🍀\t\tWinning amount:\tBet amount *2"
      "\n\t7/🍊/🍒/🍀\t\t\t  ______\t\t\t  ______\t\t\t7/🍊/🍒/🍀\t\tWinning amount:\tFree spin") #Rule and condition to win the game, able to change it later


print("\n2. Pass all four levels of status: \n\t2 wins \t\tlevel 1\t\t🖤 \n\t3 wins \t\tlevel 2\t\t🖤🖤 \n\t4 wins \t\tlevel 3\t\t🖤🖤🖤 \n\t5 wins \t\tlevel 4\t\t🖤🖤🖤🖤")
print("")
print("LET THE GAMES BEGIN...")


firstsq = None #variable for first slot
secondsq = None #variable for second slot
thirdsq = None #variable for third slot
fourthsq = None #variable for fourth slot

while True: #Create loop
    #add detailed comment
    itemlist = choose_options()
    player_tree = create_tree(current_level, level_hearts)
    display_tree(player_tree)


    while credit > 0: #While user still have credits
        print("\033[1m\nAccount Balance: £", credit, "\nAccount Status:", level_hearts[current_level], "\033[1m") #printing and updating the account information
        bet_amount_input = input("Please:"
                                 "\n\tenter bet amount"
                                 "\n\tor type '0' for free trial"
                                 "\n\tor type 'history' to see your last 5 round history and all-time winrate, "
                                 "\n\tor type 'quit' to exit the game."
                                 "\n\tType here: ") #Asking how much user want to place a bet, if user want to try the spin type'0', want to exit program type 'quit'
        if bet_amount_input.lower() == "quit": #change user input into lowercase and if input == 'quit'
            break #break the loop

        elif bet_amount_input.lower() == "history":  #change user input into lowercase and if input == 'history'
           if slothistory.get_history(): #checkk if history empty or not
                displayhistory(slothistory.get_history()) #call function to print history and winrate
                time.sleep(1.5)
           else:
               print("\nNo history available yet.")
           continue #restart the loop

        if bet_amount_input.isdigit(): #if user input is in degit
            bet_amount = int(bet_amount_input) #change user input into integer format
            if bet_amount > credit: #check if bet amount is higher than user's credits
                print("Not enough credit, please try again.") #show error message
                continue #go back to start

        elif bet_amount_input.lower() == '0': #if user input == 0
            bet_amount = 0 #given bet amount = 0 and start free trial round
        else:
            print("Invalid input, please try again.")  # show error message  /  error handling
            continue

        credit -= bet_amount  # update credits balance after putting the bet
        firstsq = random.choice(itemlist)  # random first symbol using the random function
        secondsq = random.choice(itemlist)  # random second symbol using the random function
        thirdsq = random.choice(itemlist)  # random third symbol using the random function
        fourthsq = random.choice(itemlist)  # random fourth symbol using the random function
        print("Stake accepted. Good luck.")
        print("Spinning now...")
        totalround+=1 #count totalround that have been played
        time.sleep(1)  # delay the program for 1 second
        # designing the way the slot will display
        print()

        print("| ", random.choice(itemlist), " | ", random.choice(itemlist), " | ", random.choice(itemlist), " | ", random.choice(itemlist), " | ")
        print('------------------------------')

        print("| ", firstsq, " | ", secondsq, " | ", thirdsq, " | ", fourthsq, " | ")  # show the result after spin
        print('------------------------------')

        print("| ", random.choice(itemlist), " | ", random.choice(itemlist), " | ", random.choice(itemlist), " | ", random.choice(itemlist), " | ")
        print()
        # adding different ways to win
        bet_win = 0
        if firstsq == secondsq == thirdsq == fourthsq:
            bet_win = bet_amount * 5
        elif firstsq == secondsq == thirdsq == fourthsq in ['🍒', '🍉', '🐱']:
            bet_win = bet_amount * 20
        elif firstsq == thirdsq:
            bet_win = bet_amount * 2
        elif secondsq == fourthsq:
            bet_win = bet_amount * 2
        elif (firstsq == secondsq == '🍊' or firstsq == secondsq == "🍇" or firstsq == secondsq == '🐭') and (thirdsq in ['🍊', '🍇', '🐭', '🍒', '🍉', '🐱']):
            bet_win = bet_amount * 3
        elif (firstsq == secondsq) and (firstsq in ['7', '🍏', '🐶']):
            bet_win = bet_amount * 2


        if bet_win > 0:
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

                print()

                print("| ", random.choice(itemlist), " | ", random.choice(itemlist), " | ", random.choice(itemlist),
                      " | ", random.choice(itemlist), " | ")
                print('------------------------------')

                print("| ", firstsq, " | ", secondsq, " | ", thirdsq, " | ", fourthsq,
                      " | ")  # show the result after spin
                print('------------------------------')

                print("| ", random.choice(itemlist), " | ", random.choice(itemlist), " | ", random.choice(itemlist),
                      " | ", random.choice(itemlist), " | ")
                print()

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
                elif (firstsq == secondsq) and (firstsq in ['7', '🍏', '🐶']):
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

        # added new element
        if search_for_winning_bonus(firstsq, secondsq, thirdsq, fourthsq):
            bonus_money = 200  # bonus money
            credit += bonus_money
            print(f"Congratulations! You've spun the bonus combination twice and won £{bonus_money}!")

        # added new element
        if search_for_winning_jackpot(firstsq, secondsq, thirdsq, fourthsq):
            jackpot_money = 500  # jackpot money
            credit += jackpot_money
            print(f"Congratulations! You've spun the jackpot combination five times and won £{jackpot_money}!")

        # Check if the user beat the game
        if current_level == 4 and credit >= 500 and all(heart == "🖤🖤🖤🖤" for heart in level_hearts.values()):
            print("Congratulations! You've collected the diamond 💎 and you've beat the game!")
            break

        # Check if the current level requirement is met
        if current_level < 4 and level_wins[current_level] >= wins_to_unlock_hearts[current_level]:
            current_level += 1
            player_tree = create_tree(current_level, level_hearts)
            display_tree(player_tree)

        addspinhistory(bet_amount,bet_win, [firstsq,secondsq,thirdsq,fourthsq])


    print("Thank you for playing.")
    sorted_winnings = sorted(winnings.items(), key=lambda x: x[1], reverse=True)
    print("\nWinnings sorted from highest to lowest:")
    for round_num, win_amount in sorted_winnings:
        print(f"Round {round_num}: £{win_amount}")
    print("Exiting the game...")
    time.sleep(1.5)
    break  # exit the game

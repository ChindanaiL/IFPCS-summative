import random
import time
from collections import Counter

itemlist = [" 7","🍊","🍒","🍀"] #list of item in our slot machine, able to change it later


wins_to_unlock_hearts = {  #defining the win requirments needed to unlock hearts for each level
    1: 2,
    2: 3,
    3: 4,
    4: 5,
}

level_wins = Counter() #add my detailed comment

level_hearts = { #add my detailed comment
    1: None,
    2: None,
    3: None,
    4: None
}

#add my detailed comment
class TreeNode:
    def __init__(self, level, heart):
        self.level = level
        self.heart = heart
        self.left = None
        self.right = None

root = TreeNode(1, "🖤")
root.left = TreeNode(2, "🖤🖤")
root.right = TreeNode(3, "🖤🖤🖤")
root.left.left = TreeNode(4, "🖤🖤🖤🖤")    #not working properly


#add my detailed comment
def unlock_hearts():
    for level in level_wins.keys():
        wins_required = wins_to_unlock_hearts[level]
        if level_wins[level] >= wins_required and level_hearts[level] is None:
            if level == 1:
                level_hearts[level] = "🖤"
            elif level == 2:
                level_hearts[level] = "🖤🖤"
            elif level == 3:
                level_hearts[level] = "🖤🖤🖤"
            elif level == 4:
                level_hearts[level] = "🖤🖤🖤🖤"
            print(f"Congratulations! You've unlocked the heart for Level {level}: {level_hearts[level]}")


print("")
print("                               ꧁  𝐖𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 𝐭𝐡𝐞 𝐂𝐃𝐆 𝐒𝐥𝐨𝐭 𝐌𝐚𝐜𝐡𝐢𝐧𝐞  ꧂") #the welcome message
print("")
print("        \033[1mTo beat the game you must complete two main requirements and collect the diamond --> 💎\033[1m") #using ANSI escape sequences to bold text
print("")
print("Item list: ", itemlist)
print("\n1. Earn £500. You will start with £100 and gain more based off achieving the following winning combinations:\n\t   🍊/🍀\t\t\t   🍊/🍀\t\t\t   🍊/🍀\t\t\t   🍊/🍀\t\tWinning amount:\tBet amount *5"
      "\n\t\t🍒\t\t\t\t\t🍒\t\t\t\t\t🍒\t\t\t\t\t🍒\t\t\tWinning amount:\tBet amount *20\n\t\t7\t\t\t\t\t7\t\t\t\t\t7\t\t\t\t\t7\t\t\tWinning amount:\tBet amount *15"
      "\n\t7/🍊/🍒/🍀\t\t\t  ______\t\t\t7/🍊/🍒/🍀\t\t\t  ______\t\tWinning amount:\tBet amount *3\n\t  ______\t\t\t7/🍊/🍒/🍀\t\t\t  ______\t\t\t7/🍊/🍒/🍀\t\tWinning amount:\tBet amount *3"
      "\n\t\t🍒\t\t\t\t\t🍒\t\t\t\t  ______\t\t\t  ______\t\tWinning amount:\tBet amount *5\n\t  ______\t\t\t\t🍒\t\t\t\t\t🍒\t\t\t\t  ______\t\tWinning amount:\tBet amount *5"
      "\n\t7/🍊/🍒/🍀\t\t\t  ______\t\t\t  ______\t\t\t7/🍊/🍒/🍀\t\tWinning amount:\tFree spin") #Rule and condition to win the game, able to change it later

print("\n2. Pass all four levels of status: \n\t2 wins \t\tlevel 1\t\t🖤 \n\t3 wins \t\tlevel 2\t\t🖤🖤 \n\t4 wins \t\tlevel 3\t\t🖤🖤🖤 \n\t5 wins \t\tlevel 4\t\t🖤🖤🖤🖤")
print("")
print("LET THE GAMES BEGIN...")

initialcredits = 100 #initial player's credits
current_level = 1 #tracking the current level/account status

firstsq = None #variable for first slot
secondsq = None #variable for second slot
thirdsq = None #variable for third slot
fourthsq = None #variable for fourth slot
credits = initialcredits

while True: #Create loop
    while credits > 0: #While user still have credits
        print("\033[1m\nAccount Balance: £", credits, "\nAccount Status:", level_hearts[current_level], "\033[1m") #printing and updating the account information
        bet_amount_input = input("Please enter bet amount, type '0' for free trial, or type 'quit' to exit the game: ") #Asking how much user want to place a bet, if user want to try the spin type'0', want to exit program type 'quit'
        if bet_amount_input.lower() == "quit": #change user input into lowercase and if input == 'quit'
            break #break the loop
        if bet_amount_input.isdigit(): #if user input is in degit
            bet_amount = int(bet_amount_input) #change user input into integer format
            if bet_amount > credits: #check if bet amount is higher than user's credits
                print("Not enough credit, please try again.") #show error message
                continue #go back to start
        elif bet_amount_input.lower() == '0': #if user input == 0
            bet_amount = 0 #given bet amount = 0 and start free trial round
        else:
            print("Invalid input, please try again.")  # show error message
            continue

        credits -= bet_amount  # update credits balance after putting the bet
        firstsq = random.choice(itemlist)  # random first symbol using the random function
        secondsq = random.choice(itemlist)  # random second symbol using the random function
        thirdsq = random.choice(itemlist)  # random third symbol using the random function
        fourthsq = random.choice(itemlist)  # random fourth symbol using the random function
        print("Stake accepted. Good luck.")
        print("Spinning now...")
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
        elif firstsq == secondsq == thirdsq == fourthsq == '🍒':
                bet_win = bet_amount * 20
        elif firstsq == thirdsq:
                bet_win = bet_amount * 3
        elif secondsq == fourthsq:
                bet_win = bet_amount * 3
        elif firstsq == secondsq == '🍊' and (thirdsq == '🍊' or thirdsq == '7'):
                bet_win = bet_amount * 3
        elif firstsq == secondsq == '🍊':
                bet_win = bet_amount * 4
        elif firstsq == secondsq or thirdsq == fourthsq:
                bet_win = bet_amount * 5

        if bet_win > 0:
            print("You won £", bet_win)
            credits += bet_win
            level_wins[current_level] += 1  #updating the win count for the current level
            unlock_hearts()  #updating the hearts in the account status
        else:
            print("You lost")
            # from here, doing if-else condition to show the condition how to win the game.

        # free spins
        if firstsq == fourthsq:
            free_spins = random.randint(1,5) # win between 1 to 5 free spins
            print(f'you won {free_spins} free spins')

            for i in range(free_spins):
                freespinwin = 0  #initialing the freespinwin variable

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
                freespinwin = 0
                if firstsq == secondsq == thirdsq == fourthsq:
                    freespinwin = bet_amount * 5
                elif firstsq == secondsq == thirdsq == fourthsq == '🍒':
                    freespinwin = bet_amount * 20
                elif firstsq == thirdsq:
                    freespinwin = bet_amount * 3
                elif secondsq == fourthsq:
                    freespinwin = bet_amount * 3
                elif firstsq == secondsq == '🍊' and (thirdsq == '🍊' or thirdsq == '7'):
                    freespinwin = bet_amount * 3
                elif firstsq == secondsq == '🍊':
                    freespinwin = bet_amount * 4
                elif firstsq == secondsq or thirdsq == fourthsq:
                    freespinwin = bet_amount * 5

                if freespinwin > 0:
                    print("You won £", freespinwin)
                    credits += freespinwin
                else:
                    print("You lost")

        #checking if the user beat the game
        if bet_win > 0 or freespinwin > 0:
            unlock_hearts()
            #cheacking if the current level met level 4 and £500
        if current_level < 4 and level_wins[current_level] >= wins_to_unlock_hearts[current_level]:
            current_level += 1
        #relaesing the diamond
        elif current_level == 4 and initialcredits >= 500 and all(heart == "🖤🖤🖤🖤" for heart in level_hearts.values()):
            print("Congratulations! You've collected diamond 💎 and you've beat the game! ")
            break

    print("Thank you for playing.")
    time.sleep(1.5)
    break  # exit the loop, end program

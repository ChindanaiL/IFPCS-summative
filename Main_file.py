import random
import time
print("---Welcome to Slot Machine---")
print("You will start with £100, you will be asked if you want to play.\nAnswer with yes/y or no/n")
print("---The rules of the game---")
print("To win you must get one of the following combinations:\n7\t\t7\t\t7\t\t\tWinning amount:\t250$"
      "\nGOLD\tGOLD\tGOLD\t\tWinning amount:\t100$\nCLOVER\tCLOVER\tCLOVER\t\tWinning amount:\t50$"
      "\nORANGE\tORANGE\tORANGE/GOLD\tWinning amount:\t25$\nCHERRY\tCHERRY\tCHERRY\t\tWinning amount:\t15$"
      "\nCHERRY\tCHERRY\t-\t\t\tWinning amount:\t10$\nCHERRY\t-\t\t-\t\t"
      "\tWinning amount:\t5$") #Rule and condition to win the game, able to change it later
itemlist = ["7","@","*","#"] #list of item in our slot machine, able to change it later
initialcredits = 100 #initial player's credits

firstsq = None #variable for first slot
secondsq = None #variable for second slot
thirdsq = None #variable for third slot
fourthsq = None #variable for fourth slot
credits = initialcredits

while True: #Create loop
    while credits > 0: #While user still have credits
        print("You have £", credits)
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
        print('------------------------')

        print("| ", firstsq, " | ", secondsq, " | ", thirdsq, " | ", fourthsq, " | ")  # show the result after spin
        print('------------------------')

        print("| ", random.choice(itemlist), " | ", random.choice(itemlist), " | ", random.choice(itemlist), " | ", random.choice(itemlist), " | ")
        print()
        # adding different ways to win
        bet_win = 0
        if firstsq == secondsq == thirdsq == fourthsq:
            bet_win = bet_amount * 5
        elif firstsq == secondsq == thirdsq == fourthsq == '*':
                bet_win = bet_amount * 20
        elif firstsq == thirdsq:
                bet_win = bet_amount * 3
        elif secondsq == fourthsq:
                bet_win = bet_amount * 3
        elif firstsq == secondsq or secondsq == thirdsq == '*':
                bet_win = bet_amount * 5
        elif firstsq == secondsq == thirdsq == fourthsq == '7':
                bet_win = bet_amount * 15
        elif firstsq == secondsq == thirdsq == fourthsq == '*':
                bet_win = bet_amount * 5

        if bet_win > 0:
            print("You won £", bet_win)
            credits += bet_win
        else:
            print("You lost")
            # from here, doing if-else condition to show the condition how to win the game.

    print("Thank you for playing.")
    time.sleep(1.5)
    break  # exit the loop, end program


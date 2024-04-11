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
itemlist = ["7","GOLD","CLOVER","ORANGE","CHERRY"] #list of item in our slot machine, able to change it later
initialcredits = 100 #initial player's credits

firstslot = None #variable for first slot
secondslot = None #variable for second slot
thirdslot = None #variable for third slot
credits = initialcredits

while True: #create loop
      while credits > 0: #loop while user still have credits
            print("You have £", credits) #Show user how much credits they have
            try:
                  stake_amount = int(input("Please enter stake amount: ")) #Asking for stake amount
            except: #if user's input is not in integer format
                  print("Please enter a whole number of amount to stake, Please try again.") #show error message and ask for input again

            if stake_amount>credits: #if user want to stake more than credits they have
                  print("Not enough credit, please try again.") #show error message
            else:
                  credits -= stake_amount #update credits balance after put stake
                  firstslot = random.choice(itemlist) #random first symbol by using random function
                  secondslot = random.choice(itemlist) #random second symbol by using random function
                  thirdslot = random.choice(itemlist) #random third symbol by using random function
                  print("Stake accepted. Good luck.")
                  print("Spinning now...")
                  time.sleep(1) #delay the program 1 second
                  print()
                  print("| ", firstslot, " | ", secondslot, " | ", thirdslot, " |\n") #show the result after spin

                  #from here, doing if-else condition to show the condition how to win the game.
      print("You are out of credits") #if user run out of credit, show message and quit the program.
      print("Thank you for playing.")
      time.sleep(1.5)
      break #exit the loop, end program
njjijij
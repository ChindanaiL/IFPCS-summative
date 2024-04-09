import random
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

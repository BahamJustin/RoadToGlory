from Database.schema import *
from Database.createData import *
from Database.readData import *
import csv
import sys
import os
import random

# Create 2 teams to play against each other
class homeTeam:
    city = "New Orleans"
    name = "Saints"
    wins = 0
    losses = 0
    ties = 0

class awayTeam:
    city = "Atlanta"
    name = "Falcons"
    wins = 0
    losses = 0
    ties = 0

# function to perform all changes to win/loss records
def changeRecord(winners):
    print(winners.city + " wins!")

    record = f"{winners.wins}/{winners.losses}/{winners.ties}"

    print(record)

############
def main():
    newGame()

# 
def newGame():
    print("New Game?")

    choice = input("""
                        Yes
                        No
                        
                        Y or N?:""")
    
    if choice == "Y" or choice == "y":
        os.remove('league.db')
        db.connect()
        newLeague()
        menu()
    elif choice == "N" or choice == 'n':
        menu()

# Menu Function
def menu():

    print("************  RoadToGlory  **************")

    choice = input("""
                      A: Simulate Game
                      B: View League
                      Q: Exit Game

                      Please enter your choice: """)

    if choice == "A" or choice =="a":
        simulateGame()
        print()
        menu()
    elif choice == "B" or choice =="b":
        viewLeague()
        print()
        menu()
    elif choice=="Q" or choice=="q":
        db.close()
        sys.exit
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()

# simulated games and outcomes - randomly generated for now
def simulateGame():
    homeScore = 7 * random.randint(0,5)
    homeScoreStr = str(homeScore)
    awayScore = 7 * random.randint(0,5)
    awayScoreStr = str(awayScore)

    print(
    homeTeam.name + ":" + homeScoreStr +
    """ """ +
    awayTeam.name + ":" + awayScoreStr)

    if homeScore == awayScore:
        print("It's a Tie!")
    elif homeScore > awayScore:
        changeRecord(homeTeam)
    else:
        changeRecord(awayTeam)  
    
##########
main()


# simulateGame()
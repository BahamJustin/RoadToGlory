from Database.schema import *
from Database.createData import *
from Database.readData import *
from peewee import *
import csv
import sys
import os
import random

# function to perform all changes to win/loss records
def changeRecord(winners):
    print(winners + " wins!")

    # record = f"{winners.wins}/{winners.losses}/{winners.ties}"

    # print(record)

############
def main():
    db.close()
    menu()    

# 
def newGame():
    print("Are You Sure?")

    choice = input("""
                        Yes
                        No
                        
                        Y or N?:""")
    
    if choice == "Y" or choice == "y":
        os.remove('league.db')
        newLeague()
    elif choice == "N" or choice == 'n':
        return

# Menu Function
def menu():

    print("************  RoadToGlory  **************")

    choice = input("""
                      A: Simulate Game
                      B: View League
                      C: New Game?
                      Q: Exit Game

                      Please enter your choice: """)

    if choice == "a" or choice =="A":
        simulateGame()
        print()
        menu()
    elif choice == "b" or choice =="B":
        viewLeague()
        print()
        menu()
    elif choice == "c" or choice == "C":
        newGame()
        menu()
    elif choice == "q" or choice == "Q":
        db.close()
        sys.exit
    else:
        print("You must only select either A or B")
        print("Please try again")
        menu()

# simulated games and outcomes - randomly generated for now
# Current Task: Use teams from Database to simulate games - randomly chosen teams then specific
def simulateGame():
    # create 2 teams to play against each other
    class homeTeam:
        anyTeam = Team.select().order_by(fn.Random()).limit(1).get() 
        name = anyTeam.name
        city = anyTeam.city
    
    class awayTeam:
        anyTeam = Team.select().order_by(fn.Random()).limit(1).get() 
        name = anyTeam.name
        city = anyTeam.city
    
    homeScore = 7 * random.randint(0,5)
    homeScoreStr = str(homeScore)
    awayScore = 7 * random.randint(0,5)
    awayScoreStr = str(awayScore)

    if homeTeam.name == awayTeam.name:
        simulateGame()
    else:
        print(
    homeTeam.name + ":" + homeScoreStr +
    """ """ +
    awayTeam.name + ":" + awayScoreStr)
        if homeScore == awayScore:
            print("It's a Tie!")
        elif homeScore > awayScore:
            changeRecord(homeTeam.name)
        else:
            changeRecord(awayTeam.name)
    db.close()

      

    
    
##########
main()
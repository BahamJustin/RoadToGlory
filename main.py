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
                      1: Simulate Game
                      2: View League
                      3: New Game?
                      Q: Exit Game

                      Please enter your choice: """)

    if choice == "1":
        simulateGame()
        print()
        menu()
    elif choice == "2":
        viewLeague()
        print()
    elif choice == "3":
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
            changeRecord(homeTeam.city)
        else:
            changeRecord(awayTeam.city)
    db.close()

#
def viewLeague():
    choice = input("""
                    1: View All Teams
                    2: View By Conference
                    3: View By Division
                    4: Back to Menu """)      
    if choice == "1":
        viewAllTeams()
        menu()
    elif choice == "2":
        chooseConference = input("""
                                    1. NFC
                                    2. AFC
                                    """)
        if chooseConference == "1":
            teamByConf("NFC")
            viewLeague()
        elif chooseConference == "2":
            teamByConf("AFC")
            viewLeague()
    elif choice == "3":
        chooseDivision = input("""
                        1. AFC North        5. NFC North
                        2. AFC East         6. NFC East
                        3. AFC West         7. NFC West
                        4. AFC South        8.NFC South
                        """)
        if chooseDivision == "1":
            teamByDiv("AFC North")
            viewLeague()
        elif chooseDivision == "2":
            teamByDiv("AFC East")
            viewLeague()
        elif chooseDivision == "3":
            teamByDiv("AFC West")
            viewLeague()
        elif chooseDivision == "4":
            teamByDiv("AFC South")
            viewLeague()
        elif chooseDivision == "5":
            teamByDiv("NFC North")
            viewLeague()
        elif chooseDivision == "6":
            teamByDiv("NFC East")
            viewLeague()
        elif chooseDivision == "7":
            teamByDiv("NFC West")
            viewLeague()
        elif chooseDivision == "8":
            teamByDiv("NFC South")
            viewLeague()
    else:
        menu()

##########
main()
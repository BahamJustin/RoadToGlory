from Database.schema import *
# from schema import *
from peewee import fn
import sys

# db.connect()

teamTemplate = "{team.city} {team.name}"
actorTemplate = "{actor.firstName} {actor.lastName}"
playerTemplate = "{player.firstName} {player.lastName} {player.teamName_id}"

def viewAllTeams():
    # db.connect()
    print("All Teams")
    print("-" * 35)

    for team in Team.select():
        print(teamTemplate.format(team=team))
    # db.close()

# Get specific team
def teamByID(ID):
    # db.connect()
    print(ID)
    print("-" * 35)

    print(Team.get_by_id(ID).name)
    # db.close()

def teamByConf(Confs):
    # db.connect()
    print(Confs)
    print("-" * 35)

    for team in Team.select().where(Team.conf == Confs):
        print(teamTemplate.format(team=team))
    # db.close()

def teamByDiv(Divs):
    # db.connect()
    print(Divs)
    print("-" * 35)

    for team in Team.select().where(Team.div == Divs):
        print(teamTemplate.format(team=team))
    # db.close()

def viewAllPlayers():
    print("All Players")
    print("-" * 35)

    for player in Player.select():
        print(playerTemplate.format(player=player))

#  Print Player Data
def PlayersbyTeam(Team):
    # db.connect()
    print(Team)
    print("-" * 35)
    

    for player in Player.select().where(Player.teamName == Team):
        print(playerTemplate.format(player=player))

    # db.close()

def getCurrentSeason():
    currentSeason = str(Season.select().order_by(Season.id.desc()).get().year)

    print("-------------- " + currentSeason + "-----------------")
    db.close()

# PlayersbyTeam("Saints")

# db.close()
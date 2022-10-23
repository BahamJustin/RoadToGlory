from Database.schema import *
# from schema import *
from peewee import fn
import sys

# db.connect()

template = "{team.city} {team.name}"

def viewAllTeams():
    db.connect()
    print("All Teams")
    print("-" * 35)

    for team in Team.select():
        print(template.format(team=team))
    db.close()

# Get specific team

def teamByConf(Confs):
    db.connect()
    print(Confs)
    print("-" * 35)

    for team in Team.select().where(Team.conf == Confs):
        print(template.format(team=team))
    db.close()

def teamByDiv(Divs):
    db.connect()
    print(Divs)
    print("-" * 35)

    for team in Team.select().where(Team.div == Divs):
        print(template.format(team=team))
    db.close()
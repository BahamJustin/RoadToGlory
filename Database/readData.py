from Database.schema import db, Team
# from schema import db, Team
from peewee import fn
import sys

# db.connect()

template = "{team.city} {team.name} Roster Size = {team.players}"

def viewLeague():
    db.connect()
    print("All Teams")
    print("-" * 35)

    for team in Team.select():
        print(template.format(team=team))
    
    db.close()

# Get specific team

# for team in Team.select().where(Team.players > 50):
#     print(template.format(team=team))


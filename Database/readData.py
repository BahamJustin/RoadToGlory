from Database.schema import db, Team

template = "{team.city} {team.name} Roster Size = {team.players}"

def viewLeague():
    print("All Teams")
    print("-" * 35)

    for team in Team.select():
        print(template.format(team=team))

# for team in Team.select().where(Team.players > 50):
#     print(template.format(team=team))
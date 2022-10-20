from Database.schema import db, Team

teams = (
    ("Tampa Bay", "Buccaneers", 48),
    ("Carolina", "Panthers", 49),
    ("Atlanta", "Falcons", 51),
    ("New Orleans", "Saints", 52)
)

def newLeague():
    db.create_tables([Team])
    
    for team in teams:
        Team.create(city=team[0], name=team[1], players=team[2])

# saints = Team.create(city = "New Orleans", name = "Saints")

# saints.players = 52
# saints.save()
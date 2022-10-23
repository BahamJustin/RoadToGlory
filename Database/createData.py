import os
from Database.schema import *
from datetime import *
from os import *

currentYear = datetime.now().year

teams = (
    ("Buffalo", "Bills", "AFC", "AFC East"),
    ("New York", "Jets", "AFC", "AFC East"),
    ("Miami", "Dolphins", "AFC", "AFC East"),
    ("New England", "Patriots", "AFC", "AFC East"),
    ("Baltimore", "Ravens", "AFC", "AFC North"),
    ("Cinicinatti", "Bengals", "AFC", "AFC North"),
    ("Cleveland", "Browns", "AFC", "AFC North"),
    ("Pittsburg", "Steelers", "AFC", "AFC North"),
    ("Tennessee", "Titans", "AFC", "AFC South"),
    ("Indianapolis", "Colts", "AFC", "AFC South"),
    ("Jacksonville", "Jaguars", "AFC", "AFC South"),
    ("Houston", "Texans", "AFC", "AFC South"),
    ("Kansas City", "Cheifs", "AFC", "AFC West"),
    ("Los Angeles", "Chargers", "AFC", "AFC West"),
    ("Denver", "Broncos", "AFC", "AFC West"),
    ("Las Vegas", "Raiders", "AFC", "AFC West"),
    ("Philadelphia", "Eagles", "NFC", "NFC East"),
    ("New York", "Giants", "NFC", "NFC East"),
    ("Dallas", "Cowboys", "NFC", "NFC East"),
    ("Washington", "Commanders", "NFC", "NFC East"),
    ("Minnesota", "Vikings", "NFC", "NFC North"),
    ("Green Bay", "Packers", "NFC", "NFC North"),
    ("Chicago", "Bears", "NFC", "NFC North"),
    ("Detroit", "Lions", "NFC", "NFC North"),
    ("Tampa Bay", "Buccaneers","NFC", "NFC South"),
    ("Carolina", "Panthers","NFC", "NFC South"),
    ("Atlanta", "Falcons","NFC", "NFC South"),
    ("New Orleans", "Saints","NFC", "NFC South"),
    ("San Francisco", "49ers", "NFC", "NFC West"),
    ("Los Angeles", "Rams", "NFC", "NFC West"),
    ("Seattle", "Seahawks", "NFC", "NFC West"),
    ("Arizona", "Cardinals", "NFC", "NFC West"),
)

conferences = (
    ("NFC"),
    ("AFC")
)

divisions = (
    ("NFC North"),
    ("NFC South"),
    ("NFC East"),
    ("NFC West"),
    ("AFC North"),
    ("AFC South"),
    ("AFC East"),
    ("AFC West")
)

def newLeague():
    db.connect()
    db.create_tables([Season, Team, Conference, Division])

    Season.create(year=currentYear)
    
    for team in teams:
        Team.create(city=team[0], name=team[1], conf=team[2], div=team[3])
    
    db.close()



# saints = Team.create(city = "New Orleans", name = "Saints")

# saints.players = 52
# saints.save()
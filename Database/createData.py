from schema import db, Team

db.connect()
db.create_tables([Team])

saints = Team.create(
    city = "New Orleans",
    name = "Saints"
)

# saints.players = 52
# saints.save()

# teams = (
#     ("Tampa Bay", "Buccaneers"),
#     ("Carolina", "Panthers")
# )

# for team in teams:
#     Team.create(city=team[0], name=team[1])


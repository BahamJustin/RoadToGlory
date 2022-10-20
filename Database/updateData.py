from Database.schema import db, Team

# db.connect()

template = "{team.city} {team.name} Roster Size = {team.players}"

cardinals = Team(city="Arizona", name="Cardinals", players=45)

ravens = Team(
    city="Baltimore",
    name="Ravens",
    players=52
)

Team.update(players=35).where(Team.name == "Saints").execute()

# ravens.players = 50
# ravens.save()

ravens.delete_instance()
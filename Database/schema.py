from peewee import *

db = SqliteDatabase("league.db")

# Peewee video
# https://www.youtube.com/watch?v=Vk6Ptnvqr4M&ab_channel=IDGTECHtalk

# subclass
class BaseTable(Model):
    class Meta:
        database = db

# class Week(BaseTable):
#     weekID = IntegerField(null=False, index=True)
#     season = ForeignKeyField(Season, backref='weeks')

class Season(BaseTable):
    year = IntegerField(null=False, index=True)

# Create Divisions/Conferences
class Conference(BaseTable):
    name = CharField(null=False, index=True)

class Division(BaseTable):
    name = CharField(null=False, index=True)

# create team model
class Team(BaseTable):
    city = CharField(null=False, index=True)
    name = CharField(null=False, index=True)
    conf = ForeignKeyField(Conference, backref='teams')
    div = ForeignKeyField(Division, backref='teams')

    # teamID 

#     # players = IntegerField(null=True)

# class Game(BaseTable):
#     teamA = ForeignKeyField(Team, backref='games')
#     teamB = ForeignKeyField(Team, backref='games')

# Task: Create players that belong to each team
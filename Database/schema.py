from peewee import *

db = SqliteDatabase("league.db")

# Peewee video
# https://www.youtube.com/watch?v=Vk6Ptnvqr4M&ab_channel=IDGTECHtalk

# subclass
class BaseTable(Model):
    class Meta:
        database = db

# create team model
class Team(BaseTable):
    city = CharField(null=False, index=True)
    name = CharField(null=False, index=True)
    players = IntegerField(null=True)

# Task: Create players that belong to each team
from Database.schema import *
from Database.createData import *
from Database.readData import *
from peewee import *
import csv
import sys
import os
import random

# Create an 18 week Season
# def createWeek():
#     class homeTeam:
#         anyTeam = Team.select().order_by(fn.Random()).limit(1).get() 
#         name = anyTeam.name
#         city = anyTeam.city
    
#     class awayTeam:
#         anyTeam = Team.select().order_by(fn.Random()).limit(1).get() 
#         name = anyTeam.name
#         city = anyTeam.city
    
#     if homeTeam.name == awayTeam.name:
#         createWeek()
#     else:
#         print("Week 1: " + "The " + homeTeam.city + " " + homeTeam.name + " Vs. The " + awayTeam.city + " " +  awayTeam.name)
#     db.close()

# def createSeason():
#     print(random.shuffle(teams))

# createSeason()

nfcSouth = Team.select().where(Team.div == "NFC South")

div1 = list((nfcSouth))
div2 = ["Whales", "Sharks", "Piranhas", "Alligators"]
div3 = ["Cubs", "Kittens", "Puppies", "Calfs"]

print(div1)

for team in div1: 
    print(team.name)

def create_schedule(list):
    # """ Create a schedule for the teams in the list and return it"""
    s = []

    if len(list) % 2 == 1: list = list + ["BYE"]

    for i in range(len(list)-1):

        mid = int(len(list) / 2)
        l1 = list[:mid]
        l2 = list[mid:]
        l2.reverse()    

        # Switch sides after each round
        if(i % 2 == 1):
            s = s + [ zip(l1, l2) ]
        else:
            s = s + [ zip(l2, l1) ]

        list.insert(1, list.pop())

    return s

def main():
    for round in create_schedule(div1):
        for match in round:
            print(match[0], match[1])
    print
    # for round in create_schedule(div2):
    #     for match in round:
    #         print(match[0] + " - " + match[1])
    # print
    # for round in create_schedule(div3): 
    #     for match in round:
    #         print(match[0] + " - " + match[1])
    # print
    # for round in create_schedule(div1+div2+div3): 
    #     for match in round:
    #         print(match[0] + " - " + match[1])
    # print

# main()
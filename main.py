import random

class homeTeam:
    city = "New Orleans"
    name = "Saints"
    wins = 0
    losses = 0
    ties = 0

class awayTeam:
    city = "Atlanta"
    name = "Falcons"
    wins = 0
    losses = 0
    ties = 0

def changeRecord(winners):
    print(winners.city + " wins!")

    record = f"{winners.wins}/{winners.losses}/{winners.ties}"

    print(record)

def simulateGame():
    homeScore = 7 * random.randint(0,5)
    homeScoreStr = str(homeScore)
    awayScore = 7 * random.randint(0,5)
    awayScoreStr = str(awayScore)

    print(
    homeTeam.name + ":" + homeScoreStr +
    """ """ +
    awayTeam.name + ":" + awayScoreStr)

    if homeScore == awayScore:
        print("It's a Tie!")
    elif homeScore > awayScore:
        changeRecord(homeTeam)
    else:
        changeRecord(awayTeam)      

simulateGame()
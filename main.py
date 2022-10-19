import random

homeTeam = 'New Orleans Saints'
awayTeam = 'Atlanta Falcons'

homeWins = 0
homeLosses = 0
homeTies = 0
awayWins = 0
awayLosses = 0
awayTies = 0  

homeRecord = f"{homeWins}/{homeLosses}/{homeTies}"
awayRecord = f"{awayWins}/{awayLosses}/{awayTies}"

def simulateGame():
    homeScore = 7 * random.randint(0,5)
    homeScoreStr = str(homeScore)
    awayScore = 7 * random.randint(0,5)
    awayScoreStr = str(awayScore)

    print(homeTeam + ":" + homeScoreStr +
    """
    """ +
    awayTeam + ":" + awayScoreStr)

    if homeScore == awayScore:
        print("It's a Tie!")
        print(homeTeam, homeRecord)
        print(awayTeam, awayRecord)
    elif homeScore > awayScore:
        print(homeTeam + " win!")
        print(homeTeam, homeRecord)
        print(awayTeam, awayRecord)
    else:
        print(awayTeam + " win!")
        print(homeTeam, homeRecord)
        print(awayTeam, awayRecord)

simulateGame()


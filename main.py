import random

# def calculateScore():
#     homeScore = str(7 * random.randint(0,5))

def simulateGame():

    homeTeam = 'New Orleans Saints'
    awayTeam = 'Atlanta Falcons'

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
    elif homeScore > awayScore:
        print(homeTeam + " win!")
    else:
        print(awayTeam + " win!")

simulateGame()
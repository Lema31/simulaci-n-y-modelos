import random
import math

def runEpics():
    epicsAmount = 200
    epicsCounter = 1
    gamesWon = 0
    gamesLost = 0
    balancesOfGamesWon = 0
    balancesOfGamesLost = 0
    while(epicsCounter <= epicsAmount):
        balance = startGame()
        if(balance > 100):
            gamesWon = gamesWon + 1
            balancesOfGamesWon = balancesOfGamesWon + balance
        else:
            gamesLost = gamesLost + 1
            balancesOfGamesLost = balancesOfGamesLost + balance
        epicsCounter = epicsCounter + 1

    averageBalanceOfGamesWon = round(balancesOfGamesWon / gamesWon,2)
    averageBalanceOfGamesLost = round(balancesOfGamesLost / gamesLost,2)
    averageBalance = round((balancesOfGamesLost + balancesOfGamesWon) / epicsAmount,2)

    print(f"Cantidad de juegos simulados: {epicsAmount}\n")
    print(f"Cantidad de juegos ganados: {gamesWon} ({(gamesWon / epicsAmount) * 100}%)")
    print(f"Cantidad de juegos perdidos: {gamesLost} ({(gamesLost / epicsAmount) * 100}%)")
    print(f"Balance promedio en juegos ganados: "
          f"{averageBalanceOfGamesWon} (+{averageBalanceOfGamesWon - 100})")
    print(f"Balance promedio en juegos perdidos: "
          f"{averageBalanceOfGamesLost} ({averageBalanceOfGamesLost - 100})")
    print(f"Balance promedio general: {averageBalance}")


def startGame():
    limit = 1000
    balance = 100
    minimumBet = 5
    currentRound = 1

    while(balance > 0 and balance < 600 and currentRound <= limit):
        currentBet = minimumBet + math.floor((balance - 100) / 50)
        if(currentBet < minimumBet):
            currentBet = minimumBet

        diceResult = random.randint(1, 6)

        if(diceResult % 2 == 0):
            balance = balance + currentBet
        else:
            balance = balance - currentBet
        currentRound = currentRound + 1

    return(balance)

runEpics()
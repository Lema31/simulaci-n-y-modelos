import random
import math

limit = 1000
balance = 100
minimumBet = 5
currentRound = 1

def startGame():
    global balance
    global currentRound

    while(balance > 0 and balance < 600 and currentRound <= limit):
        currentBet = minimumBet + math.floor((balance - 100) / 50)
        if(currentBet < minimumBet):
            currentBet = minimumBet

        diceResult = random.randint(1, 6)

        if(diceResult % 2 == 0):
            balance = balance + currentBet
        else:
            balance = balance - currentBet

        print(f"El resultado de la ronda #{currentRound} es {diceResult}")
        currentRound = currentRound + 1
    print(f"El balance final del jugador es: {balance}$")

startGame()
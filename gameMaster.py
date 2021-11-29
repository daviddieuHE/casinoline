import cases
import players
import random

def askPlayerInfos():
    players.player.creatPlayer()

def askPlayerBet():
    choice = input("Quel est votre prédiction ?")
    #bet = int(input("combien souhaitez vous parier ?"))
    return choice

def turnOfWeel():
    cases.case.creatCase()
    tourRoulette = random.randrange(0, 37)
    result = str(cases.case.roulette[tourRoulette].number) + str(cases.case.roulette[tourRoulette].color)
    return result

def check():
    choice = askPlayerBet()
    turn = turnOfWeel()
    try:
        turn.index(choice)
    except ValueError:
        print("vous avez perdu")
    else:
        print("vous avez gagné")

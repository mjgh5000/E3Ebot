import random

# dicePool = 15
# diceList = []
# successes = 0
# botchStatus = 0

def rollCall(dicePool, successes = 0, doubleTarget = 10, successTarget = 7):
    # successes = 0
    # doubleTarget = 10
    # successTarget = 7
    botchStatus = 0
    diceList = []
    for x in range(dicePool):
        currRoll = random.randrange(10)+1
        diceList.append(currRoll)
        if (currRoll >= successTarget):
            successes +=1
            if  (currRoll >= doubleTarget):
                successes +=1
                continue
        if (currRoll == 1):
            botchStatus += 1
            continue
    if (successes > 0): botchStatus = 0
    return [diceList, successes, botchStatus]

# print(diceList)
# print(f'Successes: {successes}')
# if (successes == 0) and (botchTracker):
#    print("Botch!")
        

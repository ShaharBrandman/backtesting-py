import json

"""a = "BTC": [],
        "ETH": [],
        "ADA": [],
        "SOL": [],
        "DOGE": []"""

LEVERAGE = 35
MAX_POSITIONS = 4

currentTotal = 100
budget = currentTotal / MAX_POSITIONS

print(f'Starting backtesting with {LEVERAGE}X Leverage, portoflio: {currentTotal}, budget: {budget}, maxPositions: {MAX_POSITIONS}')

with open('logs.json', 'r') as r:
    data = json.loads(r.read())
    
    pTotal = currentTotal

    #days
    for i in data:
        currentTotal = 0

        #currencies
        for j in data[i]:
            #P&L
            currencyPL = 0
            for k in data[i][j]:
                pl = float(k) * LEVERAGE
                currencyPL = currencyPL + pl
            
            aftermath = ((100 + currencyPL) * budget) / 100
            currentTotal = currentTotal + aftermath
            #print(f'{i} {j} P&L: {currencyPL}% with {LEVERAGE}X LEVERAGE P&L: {currencyPL * LEVERAGE}%, startingAmount: {budget}, current: {aftermath}')

        gain = (currentTotal * 100) / pTotal

        #idk man, makes no sense
        gain = gain - 100

        print(f'{i} currentTotal: {currentTotal}, P&L: {gain}%, previousTotal: {pTotal}')
        pTotal = currentTotal


            
        
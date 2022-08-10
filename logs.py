import json

"""a = "BTC": [],
        "ETH": [],
        "ADA": [],
        "SOL": [],
        "DOGE": []"""

LEVERAGE = 35
MAX_POSITIONS = 3

totalDayTotal = 100
budget = totalDayTotal / MAX_POSITIONS

print(f'Starting backtesting with {LEVERAGE}X Leverage, portoflio: {totalDayTotal}, budget: {budget}, maxPositions: {MAX_POSITIONS}')

with open('logs.json', 'r') as r:
    data = json.loads(r.read())
    
    pTotal = totalDayTotal

    #days
    for i in data:
        counter = 0
        totalDayTotal = 0
        #currencies
        for j in data[i]:
            if counter == MAX_POSITIONS:
                break
            else:
                counter = counter + 1
            
            #P&L
            totalCurrencyPL = 0
            for k in data[i][j]:
                pl = float(k) * LEVERAGE
                totalCurrencyPL = totalCurrencyPL + pl
            
            #budget + P&L
            aftermath = ((100 + totalCurrencyPL) * budget) / 100
            
            #total of the whole day
            totalDayTotal = totalDayTotal + aftermath
            print(f'{i} {j} P&L: {totalCurrencyPL}%, startingAmount: {budget}, current: {aftermath}')

        gain = (totalDayTotal * 100) / pTotal

        #idk man, makes no sense
        gain = gain - 100

        print(f'{i} totalDayTotal: {totalDayTotal}, P&L: {gain}%, previousTotal: {pTotal}')
        pTotal = totalDayTotal


            
        
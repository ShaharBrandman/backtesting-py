import json

LEVERAGE = 55
MAX_POSITIONS = 4
STARTING_PORTOFLIO = 100

print(f'Starting backtesting with {LEVERAGE}X Leverage, portoflio: {STARTING_PORTOFLIO}, budget: {STARTING_PORTOFLIO / MAX_POSITIONS}, maxPositions: {MAX_POSITIONS}')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

def dailyBudgetStrat(LEVERAGE, MAX_POSITIONS, STARTING_PORTOFLIO):
    print('Running daily budget strat')
    
    totalDayTotal = STARTING_PORTOFLIO
    budget = totalDayTotal / MAX_POSITIONS
    with open('logs.json', 'r') as r:
        data = json.loads(r.read())
        
        pTotal = totalDayTotal
        wins = 0
        loss = 0
        plWin = 0
        plLoss = 0

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
                    
                    if pl > 0:
                        wins = wins + 1
                    else: 
                        loss = loss + 1
                    
                    totalCurrencyPL = totalCurrencyPL + pl
                
                if totalCurrencyPL > 0:
                    plWin = plWin + 1
                else:
                    plLoss = plLoss + 1

                #budget + P&L
                aftermath = ((100 + totalCurrencyPL) * budget) / 100
                
                #total of the whole day
                totalDayTotal = totalDayTotal + aftermath
                #print(f'{i} {j} P&L: {totalCurrencyPL}%, startingAmount: {budget}, current: {aftermath}')

            totalGain = (totalDayTotal * 100) / STARTING_PORTOFLIO
            gain = (totalDayTotal * 100) / pTotal

            #idk man, makes no sense
            gain = gain - 100
            totalGain = totalGain - 100

            print(f'{i} totalDayTotal: {totalDayTotal}, daily P&L: {gain}%, actual P&L: {totalGain}, previousTotal: {pTotal}')
            pTotal = totalDayTotal

        accuracy = (wins * 100) / (wins + loss)
        profitChance = (plWin * 100) / (plWin + plLoss)
        
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print(f'accuracy of: {accuracy}% with {wins} wins and {loss} losses but with Profit chance of: {profitChance}%')

def onSpotBudgetStrat(LEVERAGE, MAX_POSITIONS, STARTING_PORTOFLIO):
    print('Running on spot budget strat')

    totalDayTotal = STARTING_PORTOFLIO
    budget = totalDayTotal / MAX_POSITIONS
    with open('logs.json', 'r') as r:
        data = json.loads(r.read())
        
        pTotal = totalDayTotal
        wins = 0
        loss = 0
        plWin = 0
        plLoss = 0

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
                aftermath = budget
                for k in data[i][j]:
                    pl = float(k) * LEVERAGE
                    
                    if pl > 0:
                        wins = wins + 1
                    else: 
                        loss = loss + 1

                    #budget + P&L
                    aftermath = ((100 + pl) * aftermath) / 100
                    #print(f'{i} {j} new position P&L: {pl}%, startingAmount: {budget}, current: {aftermath}')
                
                #total of the whole day
                totalDayTotal = totalDayTotal + aftermath

            totalGain = (totalDayTotal * 100) / STARTING_PORTOFLIO
            gain = (totalDayTotal * 100) / pTotal

            #idk man, makes no sense
            gain = gain - 100
            totalGain = totalGain - 100

            print(f'{i} totalDayTotal: {totalDayTotal}, daily P&L: {gain}%, actual P&L: {totalGain}, previousTotal: {pTotal}')
            pTotal = totalDayTotal

        accuracy = (wins * 100) / (wins + loss)
        
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print(f'accuracy of: {accuracy}% with {wins} wins and {loss} losses')
            

if __name__ == '__main__':
    onSpotBudgetStrat(LEVERAGE, MAX_POSITIONS, STARTING_PORTOFLIO)
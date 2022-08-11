import json

LEVERAGE = 45
MAX_POSITIONS = 4
STARTING_PORTOFLIO = 100

print(f'Starting backtesting with {LEVERAGE}X Leverage, portoflio: {STARTING_PORTOFLIO}, budget: {STARTING_PORTOFLIO / MAX_POSITIONS}, maxPositions: {MAX_POSITIONS}')
print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

def dailyBudgetStrat(LEVERAGE, MAX_POSITIONS, STARTING_PORTOFLIO):
    print('Running daily budget strat (100% Portfolio)')
    
    totalDayGainInMoney = STARTING_PORTOFLIO
    budget = totalDayGainInMoney / MAX_POSITIONS
    with open('logs.json', 'r') as r:
        data = json.loads(r.read())
        
        previousPortofolio = totalDayGainInMoney
        wins = 0
        loss = 0
        plWin = 0
        plLoss = 0

        #days
        for i in data:
            counter = 0
            totalDayGainInMoney = 0

            #currencies
            for j in data[i]:
                #limit the amount of positions active at the same time in the same day
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
                totalDayGainInMoney = totalDayGainInMoney + aftermath
                #print(f'{i} {j} P&L: {totalCurrencyPL}%, startingAmount: {budget}, current: {aftermath}')

            #total dailyGainPercentage since the start of the run
            totalGainPercentage = (totalDayGainInMoney * 100) / STARTING_PORTOFLIO

            #daily dailyGainPercentage
            dailyGainPercentage = (totalDayGainInMoney * 100) / previousPortofolio

            #idk man, makes no sense
            dailyGainPercentage = dailyGainPercentage - 100
            totalGainPercentage = totalGainPercentage - 100

            print(f'{i} totalDayGainInMoney: {totalDayGainInMoney}, daily P&L: {dailyGainPercentage}%, actual P&L: {totalGainPercentage}, previousPortofolio: {previousPortofolio}')
            
            previousPortofolio = totalDayGainInMoney

        accuracy = (wins * 100) / (wins + loss)
        profitChance = (plWin * 100) / (plWin + plLoss)
        
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print(f'accuracy of: {accuracy}% with {wins} wins and {loss} losses but with Profit chance of: {profitChance}%')

def onSpotBudgetStrat(LEVERAGE, MAX_POSITIONS, STARTING_PORTOFLIO):
    print('Running on spot budget strat (100% Portfolio)')

    totalDayGainInMoney = STARTING_PORTOFLIO
    budget = totalDayGainInMoney / MAX_POSITIONS
    with open('logs.json', 'r') as r:
        data = json.loads(r.read())
        
        previousPortofolio = totalDayGainInMoney
        wins = 0
        loss = 0

        #days
        for i in data:
            counter = 0
            totalDayGainInMoney = 0

            #currencies
            for j in data[i]:
                #limit the amount of positions active at the same time in the same day
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

                    pAftermath = aftermath

                    #budget + P&L
                    aftermath = ((100 + pl) * aftermath) / 100
                    #print(f'{i} {j} new position P&L: {pl}%, startingAmount: {pAftermath}, current: {aftermath}')
                
                #total of the whole day
                totalDayGainInMoney = totalDayGainInMoney + aftermath

            budget = totalDayGainInMoney / MAX_POSITIONS
            totalGainPercentage = (totalDayGainInMoney * 100) / STARTING_PORTOFLIO
            dailyGainPercentage = (totalDayGainInMoney * 100) / previousPortofolio

            #idk man, makes no sense
            dailyGainPercentage = dailyGainPercentage - 100
            totalGainPercentage = totalGainPercentage - 100

            print(f'{i} totalDayGainInMoney: {totalDayGainInMoney}, daily P&L: {dailyGainPercentage}%, actual P&L: {totalGainPercentage}%, previousPortofolio: {previousPortofolio}')
            previousPortofolio = totalDayGainInMoney

        accuracy = (wins * 100) / (wins + loss)
        
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print(f'accuracy of: {accuracy}% with {wins} wins and {loss} losses')
            
def coinTraderOnSpotBudgetStrat(LEVERAGE, MAX_POSITIONS, STARTING_PORTOFLIO):
    print('Running coinTrader on spot budget strat (50% Portfolio)')

    totalDayGainInMoney = STARTING_PORTOFLIO
    budget = totalDayGainInMoney / MAX_POSITIONS
    with open('logs.json', 'r') as r:
        data = json.loads(r.read())
        
        previousPortofolio = totalDayGainInMoney
        wins = 0
        loss = 0

        #days
        for i in data:
            counter = 0
            totalDayGainInMoney = 0

            #currencies
            for j in data[i]:
                #limit the amount of positions active at the same time in the same day
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

                    pAftermath = aftermath

                    #budget + P&L
                    aftermath = ((100 + pl) * aftermath) / 100
                    #print(f'{i} {j} new position P&L: {pl}%, startingAmount: {pAftermath}, current: {aftermath}')
                
                #total of the whole day
                totalDayGainInMoney = totalDayGainInMoney + aftermath

            budget = (totalDayGainInMoney / 2) / MAX_POSITIONS
            totalGainPercentage = (totalDayGainInMoney * 100) / STARTING_PORTOFLIO
            dailyGainPercentage = (totalDayGainInMoney * 100) / previousPortofolio

            #idk man, makes no sense
            dailyGainPercentage = dailyGainPercentage - 100
            totalGainPercentage = totalGainPercentage - 100

            print(f'{i} totalDayGainInMoney: {totalDayGainInMoney}, daily P&L: {dailyGainPercentage}%, actual P&L: {totalGainPercentage}%, previousPortofolio: {previousPortofolio}')
            previousPortofolio = totalDayGainInMoney

        accuracy = (wins * 100) / (wins + loss)
        
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print(f'accuracy of: {accuracy}% with {wins} wins and {loss} losses')

def coinTraderDailyBudgetStrat(LEVERAGE, MAX_POSITIONS, STARTING_PORTOFLIO):
    print('Running coinTrader daily budget strat (50% Portfolio)')
    
    totalDayGainInMoney = STARTING_PORTOFLIO
    budget = (totalDayGainInMoney / 2) / MAX_POSITIONS
    with open('logs.json', 'r') as r:
        data = json.loads(r.read())
        
        previousPortofolio = totalDayGainInMoney
        wins = 0
        loss = 0
        plWin = 0
        plLoss = 0

        #days
        for i in data:
            counter = 0
            totalDayGainInMoney = 0

            #currencies
            for j in data[i]:
                #limit the amount of positions active at the same time in the same day
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
                totalDayGainInMoney = totalDayGainInMoney + aftermath
                #print(f'{i} {j} P&L: {totalCurrencyPL}%, startingAmount: {budget}, current: {aftermath}')

            #total dailyGainPercentage since the start of the run
            totalGainPercentage = (totalDayGainInMoney * 100) / STARTING_PORTOFLIO

            #daily dailyGainPercentage
            dailyGainPercentage = (totalDayGainInMoney * 100) / previousPortofolio

            #idk man, makes no sense
            dailyGainPercentage = dailyGainPercentage - 100
            totalGainPercentage = totalGainPercentage - 100

            print(f'{i} totalDayGainInMoney: {totalDayGainInMoney}, daily P&L: {dailyGainPercentage}%, actual P&L: {totalGainPercentage}, previousPortofolio: {previousPortofolio}')
            
            previousPortofolio = totalDayGainInMoney

        accuracy = (wins * 100) / (wins + loss)
        profitChance = (plWin * 100) / (plWin + plLoss)
        
        print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
        print(f'accuracy of: {accuracy}% with {wins} wins and {loss} losses but with Profit chance of: {profitChance}%')

if __name__ == '__main__':
    onSpotBudgetStrat(LEVERAGE, MAX_POSITIONS, STARTING_PORTOFLIO)
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    coinTraderOnSpotBudgetStrat(LEVERAGE, MAX_POSITIONS, STARTING_PORTOFLIO)
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    dailyBudgetStrat(LEVERAGE, MAX_POSITIONS, STARTING_PORTOFLIO)
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    coinTraderDailyBudgetStrat(LEVERAGE, MAX_POSITIONS, STARTING_PORTOFLIO)
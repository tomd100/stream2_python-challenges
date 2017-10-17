
def getDailyBalances(numDays):
    
    numDays = min(numDays, len(daily_balances) - 1)
    
    startBals = daily_balances    
    printBalances=[]
    
    for i in range(numDays):
        bal1 = startBals[-1]
        bal2 = startBals[-2]
        startBals = startBals[:-1]
        balSet = [i + 1, bal1, bal2]
        printBalances = [balSet] + printBalances
    
    for balSet in printBalances:    
        print("slice starting %d day(s) ago: %r and %r" % (balSet[0], balSet[2], balSet[1]))
        
        
daily_balances = [107.92, 108.67, 109.86, 110.15, 108.67, 109.86, 110.15]

getDailyBalances(4)

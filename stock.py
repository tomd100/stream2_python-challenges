stockPrcs = [10, 7, 5, 8, 11, 9, 23]

maxProfit = 0
for i in range(len(stockPrcs)):
    for j in range(len(stockPrcs)):
        if j > i :
            maxProfit = max(maxProfit, stockPrcs[j] - stockPrcs[i])
print(maxProfit)

            
def max_profit(prices):
    min_pro=prices[0]
    best=0
    for i in range(1,len(prices)):
        p=prices[i]
        if p<min_pro:
            min_pro=p
        else:
            profit=p-min_pro
            if profit>best:
                best=profit
            
    return best
prices=[2, 4, 1]
print(max_profit(prices))

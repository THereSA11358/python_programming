#best buy and sell-leetcode121
prices=[7,1,5,6,3,4]
currentsum=0
maxprofit=0
for i in range(1,len(prices)):
    diff=prices[i]-prices[i-1]
    currentsum=max(0,currentsum+diff)
    maxprofit=max(maxprofit,currentsum)
print(maxprofit)


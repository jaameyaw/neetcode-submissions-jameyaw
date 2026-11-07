'''
we need a variable to keep track of the maximum we've seen so far
have nested loop

basically i on ith day 
j on i+1th day
compare and subsratct 
store in profit 

now 
if there's not profit return 0 otherwise 
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0

        for i in range(len(prices)-1):
            sell = prices[i]

            for j in range(i+1, len(prices)-1):
                buy = prices[j]

                if buy > sell:
                    profit = buy - sell
                
                    max_profit = max(profit, max_profit)

        return max_profit


'''
we need a variable to keep track of the maximum we've seen so far
have nested loop

basically i on ith day 
j on i+1th day
compare and subsratct 
store in profit 

now 
if there's not profit return 0 otherwise 

optimal Solution

prices = [10, 1, 5, 6, 7, 1]
              ^
                       ^
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, r = 0, 1
        max_profit = 0
        n = len(prices)-1

        
        while r < n:

            if prices[r] > prices[l]:
                profit = prices[r] - prices[l]

                max_profit = max(profit, max_profit)
            else:
                l = r

            r += 1
        return max_profit

        

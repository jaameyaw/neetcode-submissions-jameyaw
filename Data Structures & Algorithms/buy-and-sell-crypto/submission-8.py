'''

nested loop

i at start
j(i+1 - len(nums))

prices = [10,15,1,5,6,7,1]
                ^
                ^
max = traeck our max prof we've seen

let's go two pointers
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l, r = 0, 1
        maximum = 0

        while r<len(prices):

            if prices[l] < prices[r]:
               profit = prices[r] - prices[l]
               
               maximum = max(maximum, profit)
            else:
                l = r
            r += 1
        
        return maximum
            
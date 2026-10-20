'''
nums = [1,1,0,1,1,1]

          ^

max_len = 0
consec_len = 0
flag = 1

consec_len = 1
max_len = 2


perfomre atraversal 
if the number[i] = flag
we increase the consec_len by 1

max_len = max(consec_len, max_len)
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max_consec = 0
        consec_len = 0
        

        for num in nums:
            if num == 1:
                consec_len += 1
            else:
                consec_len = 0
            
            max_consec = max(consec_len, max_consec)
    
        return max_consec
        

        
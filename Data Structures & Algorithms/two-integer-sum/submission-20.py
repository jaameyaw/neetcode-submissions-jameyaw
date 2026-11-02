'''

hash map 
key>> value
value : index
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}

        for i,n in enumerate(nums):

            remainder = target - n

            if remainder in freq:
                return [freq[remainder], i]
            
            freq[n] = i
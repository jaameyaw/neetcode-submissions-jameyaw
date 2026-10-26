class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        count = {}

        for i,n in enumerate(nums):

            prev = target - n

            if prev in count:
                return [count[prev], i]
            
            count[n] = i

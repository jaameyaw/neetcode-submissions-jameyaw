class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #use hash map to keep track of the current number 
        #and check if we've already seen the diff (target-num)

        prevMap = {} #value to index

        for i, n in enumerate(nums):
            diff = target - n

            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        #brute force
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        #hash map #single pass through
        prev = {}

        for i, n in enumerate(nums):
            diff = target - n

            if diff in prev:
                return [prev[diff], i]
            prev[n] = i



        

        

        
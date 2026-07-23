class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #perform

        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
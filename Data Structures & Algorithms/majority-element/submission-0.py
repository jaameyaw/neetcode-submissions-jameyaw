class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        mid = n / 2
        count = 0

        # nums.sort()

        # for i in range(n):
        #     if nums[i] == nums[i+1]:
        #         count += 1
        #         if count 
        
        # brute force 
        for num in nums:
            count = sum(1 for i in nums if i == num)

            if count > n // 2:
                return num
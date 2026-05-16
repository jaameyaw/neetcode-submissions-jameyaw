class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #sort method

        if not nums:
            return 0
        
        nums.sort()

        longest_streak = 1
        curr_streak = 1

        for i in range(1, len(nums)):
            #if it's duplicate, just skip it
            if nums[i] == nums[i-1]:
                continue
            #if it's consective, grow the current chain

            elif nums[i] - nums[i-1] == 1:
                curr_streak += 1
            #the streak broke, save the max and reset the current streak
            else:
                longest_streak = max(longest_streak, curr_streak)
                curr_streak = 1
        return max(longest_streak, curr_streak)
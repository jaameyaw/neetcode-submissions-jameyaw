class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #convert array ds to use hash map for (1) look up

        numSet = set(nums)
        maxlen = 0
        for n in nums:
            if (n-1) not in numSet:
                length = 1

                while (n + length) in numSet:
                    length += 1
                maxlen = max(length, maxlen)
        return maxlen
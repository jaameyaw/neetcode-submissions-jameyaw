class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # a set to track whether an item is present or not

        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
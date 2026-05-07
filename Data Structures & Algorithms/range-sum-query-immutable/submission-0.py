class NumArray:

    def __init__(self, nums: List[int]):
        #initialize a prefix:
        self.prefix = []

        prefix = [0] * len(nums)
        prefix[0] = nums[0]

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        rightSum = self.prefix[right]
        leftSum = self.prefix[left-1] if left > 0 else 0
        return rightSum - leftSum


        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
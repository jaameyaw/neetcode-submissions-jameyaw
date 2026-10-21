'''
nums  = [3, 2, 2, 3] val = 3
[2,3,2,3]
[2,2,3,3]

k = 0


traverse thru the list; 
if the num = val 
swap with the next numb
increase the k by 1

[2,2,_, _]

'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        l = 0

        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        return l

        
        
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #array of nums
        #we need the len of the longest consecutive sequence of elmnts that can be formed

        #what is a consecutive sequence?
    #basically, each elmt is exactly 1 great than the previous elmet
    #in other words, their diff is = 1

    #ologn
    #sort the entire arra
    #compare n get the diff, if equals 1 add to res

        nums.sort()

        res = set()
#[2,20,4,10,3,4,5]
#[2,3,4,4,5,10,20]
        for i in range(1, len(nums)):
            if nums[i] - nums[i-1] == 1:
                res.add(nums[i])
                res.add(nums[i-1])
        return len(list(res))

#res = [2,3,3,4,4,5]
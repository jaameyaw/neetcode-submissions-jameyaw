'''
im thinking for the brute nested loop
i stays of the left, and j(nested loop) loops from i+1 to  ne
we will if any of the possiblites == targer
retunr i, j


perfomr an iteration to tmap the value to heir index
hash map
value:index pair

{
3:0,
4:1,
5:2,
6:3
}

perform traversla on the array
remainder =subtract nums[i] from target

if remainder in hashmap:
    return i, and hashmap[remainder]

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        count = {}

        for i,n in enumerate(nums):
            prev = target - n

            if prev in count:
                return [count[prev], i]
            count[n] = i



        
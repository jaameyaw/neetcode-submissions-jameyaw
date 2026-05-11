class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
#[3,4,5,6]
        prevMap = {}
#i = 0, 1
#n = 3, 3
        for i in range(len(nums)):
            currentN = nums[i] 
            diff = target - currentN
            #4 = 7-3
            #3 = 7-4
            

            if diff in prevMap:
                return [prevMap[diff], i]
                #return [0, 1]
            prevMap[currentN] = i
        #prevMap {3:0}
                

        
        
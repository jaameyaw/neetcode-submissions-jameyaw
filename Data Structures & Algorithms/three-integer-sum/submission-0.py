class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #three sum.
        #brute force approach --> have three nested for loops. 
        #then add the numbers to get it's sum to 0..
        #but that is o(n)^3


        #optimized Solution

        #begin by sorting the array so you've the numbers in a numbered line
        #because in order to get zero; you can pick one number and check 
        #whether sum of any other two numbers give you the the opposte of the first number
        #if the two numbers doesnt then you check if sum > 0; reduce the right side
        #if sum < 0; increase the left side
        #[-1, 0, 1, 2, -1, -4]

    #sorted [-4, -1, -1, 0, 1, 2]

        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i-1] == nums[i]: #check for duplicates and skip
                continue
                
            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = nums[i] + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1 
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l +=1 
                    #handles duplicates in finding the remaining two numbers
                    while nums[l] == nums[l - 1] and l < r:
                        l +=1

        return res




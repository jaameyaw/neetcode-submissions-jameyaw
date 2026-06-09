'''
#array find three nums distinct

sort the array to get the numbers from negative to 0 to positive

[-4,-1,-1,0,1,2]

sum = 0
traverse the entire array
pick one number i, have two pointers (i+1, and the end of the arr)
check if the two pointers sum up to the opposite of i
if results is < 0 move the left pointer foward, if results is > 0 move the right pointer backward

#check for repititions for i, if i > 0 and nums[i] == nums[i-1]; skip


i + (-i) = 0

#handle duplicates 
while l<=r and nums[l] == nums[l-1]
l+1 
continue
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            
            while l<r:
                threeSum = nums[i] + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                    continue
                elif threeSum < 0:
                    l += 1
                    continue
                else:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    while l<=r and nums[l] == nums[l-1]:
                        l += 1
                        
        return result







class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #use two pointers
        #left = 0
        #right = len(n) + 1

        #add the pointers and check if sum 
        # is 
        # sum < target
          
        l = 0
        r = len(numbers)-1

        while l < r:
            if l > 1 and numbers[l] == numbers[l-1]:
                continue
            
            if (numbers[l] + numbers[r] < target):
                l += 1
            elif (numbers[l] + numbers[r] > target):
                r -= 1
            else:
                return [l+1, r+1]
        return []

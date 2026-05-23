class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l = 0
        r = len(numbers) - 1

        while l < r:
            if l > 0 and numbers[l] == numbers[l-1]:
                continue

            twoSum = numbers[l] + numbers[r]

            if twoSum < target:
                l += 1
            elif twoSum > target:
                r -= 1
            else:
                return [l+1, r+1]
        return []
'''
initialse a hash map with 
traverse throuhg the arr
key being char count map to char as value

sort the keys then add them to add array
traverse through the array from the end return k most frequent numbers
'''



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        count = {}

        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        res = []

        for num, c in count:
            res.append()
        sorted(res)

        ans = []
        for i in range(len(res)-1, -1, -1):
            ans.append(res[i])

            if len(ans) > k-1:
                return ans
        
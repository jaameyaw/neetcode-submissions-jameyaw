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

        for num in nums:
            count[num] = count.get(num, 0) + 1

        freq = [[] for _ in range(len(nums)+1)]

        for n, c in count.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq)-1, 0, -1):
            for j in freq[i]:
                res.append(j)
            if len(res) == k:
                return res
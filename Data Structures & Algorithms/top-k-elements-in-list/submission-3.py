class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #get the frequency of the char

        numsCount = {}

        for num in nums:
            numsCount[num] = numsCount.get(num, 0) + 1
        
        freq = [[] for _ in range(len(nums)+1)]

        for n, c in numsCount.items():
            freq[c].append(n)
    #freq = [[1], [2], [3] ...]
        res = []

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res   
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        numsCount = {}

        for num in nums:
            numsCount[num] = numsCount.get(num, 0) + 1

        freq = [[] for _ in range(len(nums)+1)]

        for c, n in numsCount.items():
            freq[n].append(c)

        res = []

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res

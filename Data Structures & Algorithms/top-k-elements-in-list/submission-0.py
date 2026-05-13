class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #sorting approach
        #nlogn

        #have a dict to store their frequences

        numsCount = {}

        for num in nums:
            numsCount[num] = numsCount.get(num, 0) + 1
        
        arr = []
        for n, count in numsCount.items():
            arr.append([count, n])
        
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res
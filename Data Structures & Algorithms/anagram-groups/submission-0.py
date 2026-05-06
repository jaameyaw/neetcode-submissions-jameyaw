class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #def checkAnagram(strs1, strs2):
        #    if len(strs1) != len(strs2):
        #        return False
        #    return sorted(strs1) == sorted(strs2)

        #result = []

        #for i in range(len(strs)):
        #    for j in range(1, len(strs)):
        #        if checkAnagram(strs[i], strs[j]):
        #            result.append[strs[i], strs[j]]

        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            res[tuple(count)].append(s)
        return list(res.values())
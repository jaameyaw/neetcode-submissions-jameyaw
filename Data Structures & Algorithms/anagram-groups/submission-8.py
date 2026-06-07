class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a hash map to store the key (char of alphbet) & increase the the char of 
        #letter found 

        res = defaultdict(list)
        
        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c)-ord('a')] += 1

            res[tuple(count)].append(s)
        return list(list(res.values()))
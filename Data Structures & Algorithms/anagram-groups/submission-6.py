class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        #abc
        #cab
        #svd
        #vsd
        for word in strs:
            # word --> cab
            count = [0] * 26
            for char in word:
                #char ---> c 
                count[ord(char)- ord('a')] +=1 
                # count [99 - 97]
                #count[2] += 1
            res[tuple(count)].append(word)
        return list(res.values())

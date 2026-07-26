class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         
        dic = defaultdict(list)

        for str in strs:
            res = [0] * 26

            for char in str:
                res[ord(char) - ord('a')] += 1
            res = tuple(res)
            dic[res].append(str)
        
        return list(list(dic.values()))
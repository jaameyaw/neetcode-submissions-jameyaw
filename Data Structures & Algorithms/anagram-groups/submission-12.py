'''
group such anagrams in sublist
[[ana1], [ana2]...]
what is anagram>


lenfthe of how many characters are in a str


[
0,0,0, 0:
1   1 
]
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)

        for string in strs:

            count = [0] * 26

            for st in string:
                count[ord(st)- ord('a')] += 1

            res[tuple(count)].append(string)

        return list (res.values())
        
        
'''
what is an anagram?
talking about the same characters but in diff position
input: strs = ["act","pots","tops","cat","stop","hat"]

i can a dict to story key:value
key something that has/ track the count >>> we map value with exact count and add in a List

but list can not be key: so we use tuple
we can the ord of the char to check in that case for the coutn
|||

output: [[pots, tops, stop], [cat, act], [hat]]


[0, 0, 0, ..1, 0, 1] = ['act']
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        count = defaultdict(list)

        for char in strs:
            charCount = [0] * 26

            for c in char:
                charCount[ord(c) - ord('a')] += 1

            count[tuple(charCount)].append(char)

        return list(list (count.values()))
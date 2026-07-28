class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #have a defaultdict to store the str sorted as key: and sublist as values
        #I use default dict and not normal dict because i want to avoid keyerror
        #go through each word and sort the word
        #join the words into a string
        #hash map accept only unique keys
        #compare it with other words; group them when they're the same
        #convert your obj list into a list using list()

        ans = defaultdict(list)
        for str in strs:
            ans[''.join(sorted(str))].append(str)

        return (list(ans.values()))



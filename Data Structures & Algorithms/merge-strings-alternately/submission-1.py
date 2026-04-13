class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        mergeStr = []

        while i <= len(word1)-1  and i <= len(word2)-1:
            mergeStr.append(word1[i])
            mergeStr.append(word2[i])
            i += 1
        mergeStr.append(word1[i:])
        mergeStr.append(word2[i:])

        return ''.join(mergeStr)

        
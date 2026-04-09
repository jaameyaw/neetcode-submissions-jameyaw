class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # start1 = 0
        # start2 = 0
        # alternateWord = ''
        # flag = True

        # while flag:
        #     alternateWord = word1[start1] + word2[start2]
        #     start1 +=1
        #     start2 +=1

        #     if len(word1) == len(word2):
        #         if start1 == len(word1) and start2 == len(word2):
        #             flag = False
        # return alternateWord


        res = []
        i = 0

        while i < len(word1) and i < len(word2):
            res.append(word1[i])
            res.append(word2[i])
            i += 1

        res.append(word1[i:])
        res.append(word2[i:])

        return "".join(res)

        
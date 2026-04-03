class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = 0
        n = len(s)

        for i in range(n):
            if n != len(t):
                return False
            if s[i] in t: 
                count +=1
            else:
                return False

        return count == n
        
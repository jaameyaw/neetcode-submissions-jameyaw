class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        for i in range(len(s)):
            if len(s) != len(t):
                return False
        return sorted(s) == sorted(t)
            
    

        
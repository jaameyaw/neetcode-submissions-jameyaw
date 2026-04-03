class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
          

        for i in range(n):
            if n != len(t):
                return False
        
        return sorted(s) == sorted(t)

        
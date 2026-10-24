'''
but first check the len if they're nt equal return false
use counter from collections
get the frequencies of each string
return true if they're the same otherwise false
'''

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return Counter(s) == Counter(t)
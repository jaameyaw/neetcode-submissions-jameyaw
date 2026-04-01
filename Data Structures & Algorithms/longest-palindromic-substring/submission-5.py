'''
    b a b a d
      i
    l
        r

cbbd
l
   r
madam

noon
bbbbbbbbbbbbb


Single expansion to check for the longest palindrome
Double expansion

# Repeated
l = i
r = i + 1

# Single
l = i
r = i
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        results = [0,0] 
        for i in range(n):
            # single case
            start = i
            end = i

            while start >= 0 and end <= n-1 and s[start] == s[end]:
                if results[1] - results[0] + 1 < end - start + 1:
                    results[0], results[1] = start, end
                start -=1 
                end +=1
            #double case
            start = i
            end = i+1

            while start >= 0 and end <= n-1 and s[start] == s[end]:
                if results[1] - results[0] + 1 < end - start + 1:
                    results[0], results[1] = start, end
                start -=1 
                end +=1
                
        return s[results[0]:results[1]+1]


                    






























        
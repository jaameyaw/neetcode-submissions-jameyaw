class Solution:
    def longestPalindrome(self, s: str) -> str:    
        n = len(s)
        results = [0, 0]

        def expand(l: int, r: int):
            while l>=0 and r<=n-1 and s[l] == s[r]:
                if results[1]-results[0] +1 < r-l+1:
                    results[0], results[1] = l, r
                l -=1
                r +=1

        for i in range(n):
            #old case, # Check palindromes with a single-char center
            expand(i, i)

            # even case, # Check palindromes with a double-char center 
            expand(i, i+1)

            
        return s[results[0]:results[1]+1]




                
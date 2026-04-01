class Solution:
    def longestPalindrome(self, s: str) -> str:
        results = [0, 0]
        n = len(s)


        def expand (l, r):
            while l >= 0 and r <= n-1 and s[l]== s[r]:
                if results[1] - results[0] + 1 < r-l+1:
                    results[0], results[1] = l, r
                l -= 1
                r += 1

        for i in range(n):
            #even
            expand(i, i)

            #odd
            expand(i, i+1)

        return s[results[0]:results[1]+1]
            
                

        
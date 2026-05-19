class Solution:
    def isPalindrome(self, s: str) -> bool:

        #two pointers
        #start, end
        #check character's eligibilty...
        #if it's nonalpha;  move the pointer to the next char; then continue;
        #convert both to lower case and compare them 

        l = 0
        r = len(s)-1

        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            if not s[r].isalnum():
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l +=1 
            r -=1
        return True
            
                 


                
            

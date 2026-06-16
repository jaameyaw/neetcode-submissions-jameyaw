class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new_str = ''
#check for all alnum char first and store them in a new str
        for c in s:
            if c.isalnum():
                new_str += c.lower()
        
        left = 0
        right = len(new_str)- 1
#check on the new_str and chrck if they're the same 
        while left < right:
            if new_str[left] !=  new_str[right]:
                return False
            else:
                left +=1
                right -=1
        return True
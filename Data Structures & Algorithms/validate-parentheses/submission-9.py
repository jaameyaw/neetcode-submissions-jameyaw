
class Solution:
    def isValid(self, s: str) -> bool:
        isOpenClosed = {')':'(', '}':'{',']':'['}
        stack = []

        for char in s:
            if char in isOpenClosed:
                if stack and stack[-1] == isOpenClosed[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)    
        return True if not stack else False

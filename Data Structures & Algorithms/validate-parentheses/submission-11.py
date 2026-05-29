class Solution:
    def isValid(self, s: str) -> bool:
         #hash map
         #stack

        openToClose = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        stack = []

        for char in s:
            if char in openToClose:
                if stack and stack[-1] == openToClose[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        return True if not stack else False


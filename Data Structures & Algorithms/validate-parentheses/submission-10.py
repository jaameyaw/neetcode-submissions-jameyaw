class Solution:
    def isValid(self, s: str) -> bool:
        # Map each closing bracket to its corresponding opening bracket
        openToClose = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        # Initialize a stack to keep track of opening brackets
        stack = []

        # Iterate through each character in the input string
        for c in s:
            # If the character is a closing bracket
            if c in openToClose:
    # Check if the stack is not empty and the top of the stack 
                # matches the correct opening bracket
                if stack and stack[-1] == openToClose[c]:
                    stack.pop()
                else: 
                    return False
            else:
            # If it's an opening bracket, push it onto the stack
                stack.append(c)
    # The string is only valid if all opening brackets have been matched and popped
        return True if not stack else False
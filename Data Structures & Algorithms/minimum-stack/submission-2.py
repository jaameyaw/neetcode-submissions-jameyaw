class MinStack:
#designing a stack class

#push, pop, top, getMin operations.. all in O(1)

#in stack push, pop, top, all happen in constant time...

#the question is? how do we optimize getMin to run in O(1)
    def __init__(self):
        self.stack = [] # → stores all pushed values.
        self.minStack = []  # → stores the minimum so far at each level.

    def push(self, val: int) -> None:
        self.stack.append(val)   #Push val onto stack.

        if not self.minStack: #not self.minStack check if minStack is empty
            self.minStack.append(val)
        else:
            new_min = min(val, self.minStack[-1])#Compute the new minimum (between val and the current minimum on minStack).
            self.minStack.append(new_min)

    def pop(self) -> None:
        #Pop from both stack and minStack to keep them aligned.
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
                     # ^ → means the function has to return smthing

        return self.stack[-1] #return the top of stack

    def getMin(self) -> int: 
        return self.minStack[-1] #Return the top of minStack, which is the current minimum.
        

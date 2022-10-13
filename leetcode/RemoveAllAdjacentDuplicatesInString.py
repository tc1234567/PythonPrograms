class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = []
        
        for letter in s:
            if len(stack) > 0:
                if letter == stack[-1]:
                    stack.pop()
                else:
                    stack.append(letter)
            else:
                stack.append(letter)
                
        return ''.join(stack)                  

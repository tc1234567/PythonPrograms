class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        
        stack=[]
        
        for item in operations:
            if item=='C':
                stack.pop()
            elif item=='D':
                stack.append((stack[-1])*2)
            elif item=='+':
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(item))

        return sum(stack)

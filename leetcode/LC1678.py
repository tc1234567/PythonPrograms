class Solution:
    def interpret(self, command: str) -> str:

        result=''
        i=0

        while i<len(command):
            if command[i]=='G':
                result+='G'
                i+=1
            if i+1<len(command) and command[i]=='(' and command[i+1]==')':
                result+='o'
                i+=2
            if i+3<len(command) and command[i:i+4]=='(al)':
                result+='al'
                i+=4
                
        return result

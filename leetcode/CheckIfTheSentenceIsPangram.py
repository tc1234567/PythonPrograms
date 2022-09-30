class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        
        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        flag = ''
        for i in alphabet:
            if i in sentence:
                flag=True
            else:
                flag=False
                break
                
        if flag==True:
            return True
    
        return False        

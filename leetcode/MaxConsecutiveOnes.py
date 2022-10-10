class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        counter,ones=0,0
        
        for i in nums:
            if i==1:
                counter+=1
                ones=max(counter,ones)
            else:
                counter=0
                
        return ones

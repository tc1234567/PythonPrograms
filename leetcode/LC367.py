class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        first,last=1,num
        
        while first<=last:
            mid=(first+last)//2
            square=mid*mid
            if square==num: return True
            elif square>num: last=mid-1
            else: first=mid+1
        return False

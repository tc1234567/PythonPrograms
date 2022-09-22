class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        st = list(set(nums))
        
        if len(st)<=2:
            
            return max(st)
        
        else:
            
            st.remove(max(st))
            st.remove(max(st))
            
            return max(st)

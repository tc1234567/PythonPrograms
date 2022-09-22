class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        f_lst = list(set(nums))
                
        f_lst.sort()
        
        for item in f_lst:
            
            if item == 0:
                
                f_lst.remove(item)

                
            c = len(f_lst)
            
        return c
        

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        unique = []
        duplicates = []

        for i in nums:
            if i in unique:
                duplicates.append(i)
            else:
                unique.append(i)
    
        return (set(unique) - set(duplicates)).pop()

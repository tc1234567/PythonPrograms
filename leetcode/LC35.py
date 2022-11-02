class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        first,last=0,len(nums)-1

        while first<=last:
            mid=(first+last)//2
            if target==nums[mid]: return mid
            if target<nums[mid]: last=mid-1
            if target>nums[mid]: first=mid+1
            if target not in nums:
                nums.append(target)
                nums.sort()
                return nums.index(target)

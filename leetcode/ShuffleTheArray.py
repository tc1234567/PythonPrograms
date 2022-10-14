class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
      
        nums1, nums2 = nums[0:n], nums[n:2*n]
        res = list(zip(nums1,nums2))
        lst = []

        for x,y in res:
           lst.append(x)
           lst.append(y)

        return lst

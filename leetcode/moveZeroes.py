
def moveZeroes(self, nums: List[int]) -> None:

    zeroes = nums.count(0)

    for x in range(zeroes):
        for i in range(len(nums)-1):
            if nums[i] == 0 and nums[i+1] != 0:
                temp = nums[i]
                nums[i] = nums[i+1]
                nums[i+1] = temp
                   
            if nums[i] == 0 and nums[i+1] == 0:
                pass
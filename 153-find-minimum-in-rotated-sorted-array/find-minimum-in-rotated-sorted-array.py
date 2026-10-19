class Solution:
    def findMin(self, nums: list[int]) -> int:
        n=len(nums)
        guess=0
        while nums[guess]>nums[n-1]:
            guess+=1
        return nums[guess]
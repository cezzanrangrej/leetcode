class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        a=sorted(nums)
        return nums.index(a[-1])
class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        a=sorted(nums)
        n=len(a)
        return nums.index(a[n-1])
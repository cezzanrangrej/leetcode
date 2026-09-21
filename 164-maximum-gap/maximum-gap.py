class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        n=len(nums)
        if n<2:
            return 0
        nums.sort()
        mx=0
        for i in range(n-1):
            r=nums[i+1]-nums[i]
            mx=max(r,mx)
        return mx

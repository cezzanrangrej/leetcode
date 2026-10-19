class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()
        n=0
        if not nums:
            return 0
        mx=0
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==1:
                n+=1
            elif nums[i+1]==nums[i]:
                continue
            else:
                mx=max(mx,n+1)
                n=0
        mx=max(mx,n+1)
        return mx
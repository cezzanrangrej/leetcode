class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        mx=0
        c=1
        for i in range(len(nums)-1):
            if nums[i+1]-nums[i]==1:
                c+=1
            elif nums[i]==nums[i+1]:
                continue
            else:
                c=1
            mx=max(c,mx)
        mx=max(c,mx)
        return mx
class Solution:
    def eraseOverlapIntervals(self, nums: list[list[int]]) -> int:
        nums.sort(key=lambda x:x[0])
        c=0
        n=len(nums)
        end=nums[0][1]
        for i in range(1,n):
            if end>nums[i][0]:
                c+=1
                end=min(nums[i][1],end)
            else:
                end=nums[i][1]
        return c
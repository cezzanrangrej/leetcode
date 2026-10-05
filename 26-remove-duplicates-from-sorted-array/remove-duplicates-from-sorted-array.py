class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        c=0
        for i in range(1,len(nums)):
            if nums[c]==nums[i]:
                continue
            else:
                c+=1
                nums[c]=nums[i]
        return c+1
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        be=nums[0]
        ans=nums[0]
        for i in range(1,len(nums)):
            v1=be+nums[i]
            v2=nums[i]
            be=max(v1,v2)
            ans=max(be,ans)
        return ans
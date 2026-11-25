class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n=len(nums)
        dp=[1]*n
        i,j=0,0
        while i<n:
            if i==j:
                i+=1
                j=0
                continue
            if nums[i]>nums[j]:
                if dp[i]<dp[j]+1:
                    dp[i]=dp[j]+1
                
            j+=1
        return max(dp) 
class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        dp=[-1]*n
        def fun(i):
            if i>=n:
                return 0

            if dp[i]!=-1:
                return dp[i]

            dp[i]=nums[i]+max(fun(i+2),fun(i+3))

            return dp[i]

        return max(fun(0), fun(1))
        
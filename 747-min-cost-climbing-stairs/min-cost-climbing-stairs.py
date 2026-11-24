class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n=len(cost)
        dp=[-1] * n
        def fun(i):
            if i>=n:
                return 0

            if dp[i] !=-1:
                return dp[i]
            
            dp[i]=min(cost[i]+fun(i+1),cost[i]+fun(i+2))

            return dp[i]

        return min(fun(0),fun(1))
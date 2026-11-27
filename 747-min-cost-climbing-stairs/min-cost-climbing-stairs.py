class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n=len(cost)
        
        p=0
        pp=0
        ans=0

        for i in range(2,n+1):
            ans= min(p+cost[i-1], pp+cost[i-2])
            pp=p
            p=ans

        return ans
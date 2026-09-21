class Solution:
    def maxProfit(self, n: list[int]) -> int:
        mx=0
        mn=n[0]
        for i in range(1,len(n)):
            if mn<n[i]:
                r=n[i]-mn
                mx=max(mx,r)
            else:
                mn=n[i]
        return mx
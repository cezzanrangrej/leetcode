class Solution:
    def maxProfit(self, p: List[int]) -> int:
        cur=p[0]
        ans=0
        i=1
        while i<len(p):
            if cur>p[i]:
                cur=p[i]
                i+=1
            else:
                mx=p[i]-cur
                ans=max(ans,mx)
                i+=1
        return ans
class Solution:
    def rob(self, nums: list[int]) -> int:
        n=len(nums)
        
        prev=0
        prev_prev=0
        ans =0

        for i in range(n):
            ans = max(prev,prev_prev+nums[i])
            prev_prev=prev
            prev=ans

        return ans
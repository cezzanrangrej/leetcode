class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        ws = sum(nums[:k])
        mx = ws

        for i in range(k, len(nums)):
            ws = ws - nums[i-k] + nums[i]
            mx = max(mx, ws)

        return mx / k
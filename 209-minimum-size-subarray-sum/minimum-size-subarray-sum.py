class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        if sum(nums)<target:
            return 0
        n=len(nums)
        ss=0
        left=0
        mn=len(nums)+1
        for right in range(n):
            ss += nums[right]

            while ss >= target:
                mn = min(mn, right - left + 1)
                ss -= nums[left]
                left += 1

        return mn
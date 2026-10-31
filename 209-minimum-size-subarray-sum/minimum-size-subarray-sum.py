class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left=0
        right=0
        n=len(nums)
        mn=float('inf')
        sm=0
        while right<n:
            sm += nums[right]

            while sm >= target:
                l = right - left + 1
                mn = min(mn, l)

                sm -= nums[left]
                left += 1

            right += 1
        return 0 if mn == float('inf') else mn
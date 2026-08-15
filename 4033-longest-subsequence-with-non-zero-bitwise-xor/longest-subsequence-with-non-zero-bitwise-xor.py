class Solution:
    def longestSubsequence(self, nums):
        total = 0

        for n in nums:
            total ^= n

        if total != 0:
            return len(nums)

        if any(n != 0 for n in nums):
            return len(nums) - 1

        return 0
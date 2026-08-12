class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        ht = {}
        left = 0
        mx = 0

        for right in range(len(nums)):
            ht[nums[right]] = ht.get(nums[right], 0) + 1

            while ht[nums[right]] > k:
                ht[nums[left]] -= 1
                left += 1

            mx = max(mx, right - left + 1)

        return mx
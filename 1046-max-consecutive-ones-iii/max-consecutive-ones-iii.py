class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        n = len(nums)
        left = 0
        right = 0
        a = k
        mx = 0

        while right < n:
            if nums[right] == 0:
                a -= 1

            while a < 0:
                if nums[left] == 0:
                    a += 1
                left += 1

            mx = max(mx, right - left + 1)
            right += 1

        return mx
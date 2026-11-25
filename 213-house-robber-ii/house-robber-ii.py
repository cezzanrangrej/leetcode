
class Solution:
    def rob(self, nums: list[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        if n==3:
            return max(nums)

        def solve(start, end):
            dp = [-1] * n

            def fun(i):
                if i > end:
                    return 0

                if dp[i] != -1:
                    return dp[i]

                dp[i] = max(nums[i] +fun(i+2), fun(i+1))

                return dp[i]

            return fun(start)

        return max(solve(0, n-2), solve(1, n-1))

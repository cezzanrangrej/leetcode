class Solution:
    def maxProfit(self, p: List[int]) -> int:
        buy = p[0]
        profit = 0

        for i in range(1, len(p)):
            buy = min(buy, p[i])
            profit = max(profit, p[i] - buy)

        return profit
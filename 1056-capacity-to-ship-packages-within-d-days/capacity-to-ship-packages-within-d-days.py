class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        while l <= r:
            mid = (l + r) // 2

            d = 1
            total = 0

            for weight in weights:
                if total + weight > mid:
                    d += 1
                    total = 0

                total += weight

            if d <= days:
                r = mid - 1
            else:
                l = mid + 1

        return l
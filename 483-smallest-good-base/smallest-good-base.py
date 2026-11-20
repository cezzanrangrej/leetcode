class Solution:
    def smallestGoodBase(self, n: str) -> str:
        n = int(n)

        for m in range(60, 1, -1):

            low = 2
            high = n - 1

            while low <= high:
                mid = (low + high) // 2

                total = 0
                curr = 1

                for _ in range(m):
                    total += curr
                    curr *= mid

                    if total > n:
                        break

                if total == n:
                    return str(mid)

                elif total < n:
                    low = mid + 1

                else:
                    high = mid - 1

        return str(n - 1)

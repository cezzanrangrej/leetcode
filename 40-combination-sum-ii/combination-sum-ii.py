class Solution:
    def combinationSum2(self, c: list[int], target: int) -> list[list[int]]:
        c.sort()
        result, path = [], []

        def fun(start, remaining):
            if remaining == 0:
                result.append(path[:])
                return

            for i in range(start, len(c)):

                # Skip duplicates at the same level
                if i > start and c[i] == c[i-1]:
                    continue

                # Early pruning
                if c[i] > remaining:
                    break

                path.append(c[i])
                fun(i + 1, remaining - c[i])
                path.pop()

        fun(0, target)
        return result
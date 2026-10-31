
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left = 0
        ht = {}
        mx = 0

        for right in range(len(fruits)):
            ht[fruits[right]] = ht.get(fruits[right], 0) + 1

            while len(ht) > 2:
                ht[fruits[left]] -= 1

                if ht[fruits[left]] == 0:
                    del ht[fruits[left]]

                left += 1

            mx = max(mx, right - left + 1)

        return mx

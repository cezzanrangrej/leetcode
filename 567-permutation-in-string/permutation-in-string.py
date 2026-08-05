class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n > m:
            return False

        ht1 = {}
        ht2 = {}

        for ch in s1:
            ht1[ch] = ht1.get(ch, 0) + 1
        for i in range(n):
            ht2[s2[i]] = ht2.get(s2[i], 0) + 1

        left = 0
        right = n

        while True:
            if ht1 == ht2:
                return True

            if right == m:
                break

            ht2[s2[left]] -= 1
            if ht2[s2[left]] == 0:
                del ht2[s2[left]]

            ht2[s2[right]] = ht2.get(s2[right], 0) + 1

            left += 1
            right += 1

        return False
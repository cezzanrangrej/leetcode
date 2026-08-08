class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ht = {}

        for ch in t:
            if ch in ht:
                ht[ch] += 1
            else:
                ht[ch] = 1

        left = 0
        right = 0
        count = len(t)

        ans = ""

        while right < len(s):

            if s[right] in ht:
                if ht[s[right]] > 0:
                    count -= 1

                ht[s[right]] -= 1

            right += 1

            while count == 0:

                if ans == "" or right - left < len(ans):
                    ans = s[left:right]

                if s[left] in ht:
                    ht[s[left]] += 1

                    if ht[s[left]] > 0:
                        count += 1

                left += 1

        return ans
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ht = {}

        for ch in nums:
            if ch in ht:
                ht[ch] += 1
            else:
                ht[ch] = 1

        k = 0

        for key, val in ht.items():
            val = min(val, 2)

            for _ in range(val):
                nums[k] = key
                k += 1

        return k
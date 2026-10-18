class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        mx=max(arr)
        return arr.index(mx)
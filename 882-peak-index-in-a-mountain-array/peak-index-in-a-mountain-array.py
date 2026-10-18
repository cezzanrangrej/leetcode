class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        n=len(arr)
        for i in range(1,n-1):
            if arr[i-1]<arr[i]>arr[i+1]:
                return i
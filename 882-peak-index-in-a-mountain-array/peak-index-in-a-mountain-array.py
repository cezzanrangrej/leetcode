class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        n=len(arr)
        l,r=1,n-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid-1]<arr[mid]>arr[mid+1]:
                return mid
            elif arr[mid-1]>arr[mid]>arr[mid+1]:
                r=mid-1
            else:
                l=mid+1

class Solution:
    def findMin(self, nums: list[int]) -> int:
        n=len(nums)
        l,r=0,n-1
        if n==1:
            return nums[0]
        while l<=r:
            mid=(l+r)//2
            if nums[mid] <= nums[-1]:
                if nums[mid] < nums[mid-1]:
                    return nums[mid]
                r=mid-1
            else:
                l=mid+1
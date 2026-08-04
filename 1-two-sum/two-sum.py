class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        left=0
        right=left+1
        while left<n:
            if nums[left]+nums[right] == target:
                return (left,right)
                break
            elif right==n-1:
                left+=1
                right=left+1
            else:
                right+=1
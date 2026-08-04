class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mx=max(nums)
        mn=min(nums)
        ans=[]
        for i in range(mn,mx):
            if not i in nums:
                ans.append(i)
            else:
                continue
        return ans
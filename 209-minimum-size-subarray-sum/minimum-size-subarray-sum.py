class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n=len(nums)
        if sum(nums)<target:
            return 0
            sys.exit()
        som=0
        
        mn=10**5+1
        left=0
        for right in range(n):
            som+=nums[right]
            while som>=target:
                mn=min(mn,right-left+1)
                som-=nums[left]
                left+=1
        return mn

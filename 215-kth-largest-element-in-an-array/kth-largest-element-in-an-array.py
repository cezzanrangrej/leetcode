class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        import heapq
        mh=[]
        c=k
        for num in nums:
            if c>0:
                heapq.heappush(mh, num)
                c-=1
            
        for i in range(k,len(nums)):
            if nums[i]>mh[0]:
                heapq.heappushpop(mh,nums[i])
        return mh[0]
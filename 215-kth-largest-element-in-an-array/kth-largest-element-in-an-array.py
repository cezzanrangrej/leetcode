class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        import heapq
        mh=[]
        mh=nums[:k]
        heapq.heapify(mh)
            
        for i in range(k,len(nums)):
            if nums[i]>mh[0]:
                heapq.heappushpop(mh,nums[i])
        return mh[0]
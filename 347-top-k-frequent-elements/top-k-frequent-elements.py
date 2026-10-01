class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        hm=Counter(nums)
        shm=dict(sorted(hm.items(), key=lambda item:item[1], reverse=True))
        a=[]
        for i in shm:
            if k>0:
                a.append(i)
                k-=1
        return a
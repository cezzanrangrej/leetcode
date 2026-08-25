class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        i=1
        while True:
            op=i*k
            if not op in nums:
                return op
            else:
                i+=1
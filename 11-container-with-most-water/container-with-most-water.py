class Solution:
    def maxArea(self, h: List[int]) -> int:
        n=len(h)
        left=0
        right=n-1
        curr_vol=0
        max_vol=0
        while left<right:
            if h[right] > h[left]:
                curr_vol= abs(right-left) * h[left]
                left+=1
            else:
                curr_vol= abs(right-left) * h[right]
                right-=1
            max_vol = max(curr_vol,max_vol)
        return max_vol
class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        n=len(nums)
        left=[nums[0]]
        right=[nums[-1]]
        for i in range(1,n):
            left.append(left[-1]+nums[i])
        
        for j in range(n-2,-1,-1):
            right.append(right[-1]+nums[j])
        right.reverse()
            
        print(left)
        print(right)
        k=0
        while k<len(left):
            if left[k]==right[k]:
                return k
            else:
                k+=1
        return -1
         
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n=len(nums)
        closet=nums[0]+nums[1]+nums[2]
        for i in range(n-2):
            left=i+1
            right=n-1
            while left < right:
                curr=nums[i]+nums[left]+nums[right]
                curr_diff = abs(target-curr)
                clo_diff = abs(target - closet)

                if curr_diff < clo_diff:
                    closet=curr
                
                if curr > target:
                    right -= 1

                elif curr < target:
                    left +=1
                else:
                    return target

        return closet
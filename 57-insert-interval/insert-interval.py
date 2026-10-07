class Solution:
    def insert(self, nums: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        nums.append(newInterval)
        nums.sort(key=lambda x:x[0])
        ans=[]
        start1=nums[0][0]
        end1=nums[0][1]
        for i in range(1,len(nums)):
            start2=nums[i][0]
            end2=nums[i][1]
            if end1>=start2:
                start1=start1
                end1=max(end1,end2)
                continue
            else:
                ans.append([start1,end1])
                start1=nums[i][0]
                end1=nums[i][1]
        ans.append([start1,end1])
        return ans
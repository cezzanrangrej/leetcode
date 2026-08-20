class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arr1=[nums[0]]
        arr2=[nums[1]]
        print (arr1,arr2)
        for i in range(2,len(nums)):
            if arr1[-1]>arr2[-1]:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        result = arr1+arr2
        return result
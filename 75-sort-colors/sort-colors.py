class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero=0
        one=0
        two=0
        for i in range(len(nums)):
            if nums[i]==0:
                zero+=1
            elif nums[i]==1:
                one+=1
            else:
                two+=1
        nums.clear()
        nums.extend([0]*zero)
        nums.extend([1]*one)
        nums.extend([2] * two)
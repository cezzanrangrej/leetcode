class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        def fun(c, i):
            if i == len(nums)-1:
                return True

            if nums[i] > nums[i+1]:
                if c == 1:
                    return False

                c += 1

                if i == 0 or nums[i-1] <= nums[i+1]:
                    nums[i] = nums[i+1]
                else:
                    nums[i+1] = nums[i]

            return fun(c, i+1)

        return fun(0, 0)
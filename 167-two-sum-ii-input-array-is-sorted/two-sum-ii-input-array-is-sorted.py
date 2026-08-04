class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        left = 0
        right = n-1
        for _ in range(n-1):
            som =  numbers[left] + numbers[right]
            if som ==target:
                return [left+1, right+1]
                break
            elif som > target:
                right -=1
            else:
                left +=1
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        arr=list(s)
        mx=0
        ans=[]
        for right in range(len(arr)):
            while arr[right] in ans:
                ans.remove(arr[left])
                left +=1
            ans.append(arr[right])
            mx=max(mx, right - left + 1)
        return mx
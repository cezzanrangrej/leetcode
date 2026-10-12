class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        n2=len(nums2)
        st=[]
        ans=[]
        for i in range(n2-1,-1,-1):
            while st and st[-1]<=nums2[i]:
                st.pop()
            if st:
                ans.append(st[-1])
            else:
                ans.append(-1)
            st.append(nums2[i])
        ans.reverse()
        ans2=[]
        for j in range(len(nums1)):
            if nums1[j] in nums2:
                ans2.append(ans[nums2.index(nums1[j])])
        return ans2
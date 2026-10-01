class Solution:
    def longestPalindrome(self, s: str) -> int:
        n=len(s)
        one=1
        if n==1:
            return 1
        hhm=Counter(s)
        hm=dict(sorted(hhm.items(),key=lambda item:item[1],reverse=True))
        print(hm)
        count=0
        for i in hm:
            if hm[i]%2==0:
                count+=hm[i]
            elif hm[i]%2==1 and one==1:
                count+=hm[i]
                one-=1
            else:
                count+=hm[i]
                count-=1
            print(count)
        return count

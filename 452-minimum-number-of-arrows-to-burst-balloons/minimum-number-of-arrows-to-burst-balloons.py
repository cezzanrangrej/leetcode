class Solution:
    def findMinArrowShots(self, p: list[list[int]]) -> int:
        p.sort(key=lambda x:x[0])
        print(p)
        c=1
        start1=p[0][0] #1
        end1=p[0][1] #6
        for i in range(1,len(p)):
            start2=p[i][0]  #7
            end2=p[i][1]  #12
            if end1>=start2: #6>=7
                start1=start1 #1
                end1=min(end1,end2) #6
            elif end1 < start2:
                c+=1
                start1=start2
                end1=end2
                
        return c
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        cur=head
        arr=[]
        temp=[]
        gtr=[]
        j=0
        while cur:
            arr.append(cur.val)
            cur=cur.next

        for i in arr:
            if i<x:
                temp.append(i)
            else:
                gtr.append(i)
        ar=temp+gtr

        dummy=ListNode(0)
        curr=dummy
        for k in ar:
            curr.next=ListNode(k)
            curr=curr.next

        return dummy.next
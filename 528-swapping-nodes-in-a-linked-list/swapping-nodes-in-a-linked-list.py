# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head==None or head.next==None:
            return head 
        cur = head
        arr=[]
        while cur:
            arr.append(cur.val)
            cur=cur.next
        
        arr[k - 1], arr[-k] = arr[-k], arr[k - 1]

        
        dummy=ListNode(0)
        curr=dummy
        for i in arr:
            curr.next=ListNode(i)
            curr=curr.next

        return dummy.next
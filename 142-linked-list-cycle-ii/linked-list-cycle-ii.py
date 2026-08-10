# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def has(self, head: Optional[ListNode]) -> bool:
        slow=head
        fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                return slow
        return

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start=head
        inter=self.has(head)
        if not inter:
            return
        while inter != start:
            inter=inter.next
            start=start.next
        return start
            
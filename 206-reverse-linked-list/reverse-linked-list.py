# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        def fun(cur):

            if cur is None or cur.next is None:
                return cur
            newhead = fun(cur.next)
            cur.next.next=cur
            cur.next=None

            return newhead

        return fun(head)
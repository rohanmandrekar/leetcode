# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        
        dummy=ListNode()
        curr=head
        prev=dummy

        while curr and curr.next:

            nxtpair=curr.next.next
            second=curr.next

            second.next=curr
            curr.next=nxtpair   
            prev.next=second

            prev=curr
            curr=nxtpair
            

        return dummy.next or curr
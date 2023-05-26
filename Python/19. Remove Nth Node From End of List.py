# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        x=0
        curr=head
        if curr.next==None and n==1:
            return curr.next
        
        curr=head
        while curr.next!=None:
            x+=1
            curr=curr.next
        x+=1    
        print(x)  

        pt=x-n-1
        print(pt)
        curr=head
        if pt==-1:
            return curr.next
        for i in range(0,pt):
            curr=curr.next
        
        
        curr.next=curr.next.next
        return head
            
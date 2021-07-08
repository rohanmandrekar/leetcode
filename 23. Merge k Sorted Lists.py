# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        temp=[]
        tot=0
        for i in range(0,len(lists)):
            curr=lists[i]
            while curr!=None:
                temp.append(curr.val)
                curr=curr.next

        def mergesort(temp):
            if len(temp)>1:
                mid=len(temp)//2
                l=temp[:mid]
                r=temp[mid:]
                mergesort(l)
                mergesort(r)
            
                i=j=k=0
            
                while i<len(l) and j<len(r):
                    if l[i]<r[j]:
                        temp[k]=l[i]
                        i+=1
                    else:
                        temp[k]=r[j]
                        j+=1
                    k+=1
                while i <len(l):
                    temp[k]=l[i]
                    i+=1
                    k+=1
                while j<len(r):
                    temp[k]=r[j]
                    j+=1
                    k+=1
            return temp
        temp=mergesort(temp)

        dummy=ListNode()
        ans=dummy
        for num in temp:
            ans.next=ListNode(num)
            ans=ans.next
            

        return dummy.next
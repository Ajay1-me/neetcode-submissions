# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        cur = head
        while cur:
            nodes.append(cur)
            cur = cur.next

        removeIndex = len(nodes) - n
        if removeIndex == 0:
            return head.next

        nodes[removeIndex - 1].next = nodes[removeIndex].next
        return head
        
        # arr = []
        # curr = head

        # # Copy Values into an array
        # while curr:
        #     arr.append(curr.val)
        #     curr = curr.next
    
        # indexToRemove = len(arr) - n
        # arr.pop(indexToRemove)

        # # Removing the only node leaves an empty list
        # if not arr:
        #     return None

        # # Write remaining values back to the Linked List
        # curr = head
        # for j in range(len(arr)):
        #     curr.val = arr[j]
        #     if j == len(arr)-1:
        #         curr.next = None
        #     else:
        #         curr = curr.next


        # return head



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Create a dummy node
        node = dummy  # Initialize node to point at the dummy
        
        # While both lists are non-empty
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1  # Attach list1 to the result
                list1 = list1.next  # Move list1 to its next node
            else:
                node.next = list2  # Attach list2 to the result
                list2 = list2.next  # Move list2 to its next node
            node = node.next  # Move to the next node in the result list
        
        # At this point, one of the lists might still have remaining elements
        node.next = list1 or list2  # Attach the remaining elements
        
        return dummy.next  # Return the next node after dummy, which is the head of the merged list

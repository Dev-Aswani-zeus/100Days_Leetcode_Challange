# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Count nodes
        count = 0
        temp = head

        while temp:
            count += 1
            temp = temp.next

        # Move to middle
        middle = count // 2
        temp = head

        while middle:
            temp = temp.next
            middle -= 1

        return temp
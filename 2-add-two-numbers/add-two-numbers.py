# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)

        current = dummy

        carry = 0

        while l1 or l2 or carry:

            value1 = 0
            value2 = 0

            if l1:
                value1 = l1.val

            if l2:
                value2 = l2.val

            total = value1 + value2 + carry

            carry = total // 10

            digit = total % 10

            current.next = ListNode(digit)

            current = current.next

            if l1:
                l1 = l1.next

            if l2:
                l2 = l2.next

        return dummy.next
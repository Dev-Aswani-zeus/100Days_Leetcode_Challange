class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0)
        dummy.next = head
        previous = dummy
        first = head
        while first and first.next:

            second = first.next
            next_pair = second.next
            second.next = first
            first.next = next_pair
            previous.next = second
            previous = first
            first = next_pair

        return dummy.next
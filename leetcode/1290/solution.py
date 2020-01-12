# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        length = 0
        ref = head
        while ref:
            length += 1
            ref = ref.next

        current_value = 2 ** (length - 1)
        result_value = 0
        while head:
            result_value += (current_value * head.val)
            current_value //= 2
            head = head.next

        return result_value

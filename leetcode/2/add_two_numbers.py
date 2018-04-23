# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = ListNode(value)
        if self.tail:
            self.tail.next = new_node
            self.tail = self.tail.next
        else:
            self.head = new_node
            self.tail = new_node

    def get_head(self):
        return self.head

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        result_list = LinkedList()
        carry_in = 0


        while l1 and l2:
            result = l1.val + l2.val + carry_in

            current_digit = result % 10
            carry_in = result / 10

            result_list.append(current_digit)

            l1 = l1.next
            l2 = l2.next

        def resolve_carry(result_list, carry_in, list_reference):
            while list_reference:
                result = list_reference.val + carry_in
                current_digit = result % 10
                carry_in = result / 10

                result_list.append(current_digit)

                list_reference = list_reference.next
            return carry_in

        if l1:
            carry_in = resolve_carry(result_list, carry_in, l1)
        if l2:
            carry_in = resolve_carry(result_list, carry_in, l2)

        if carry_in:
            result_list.append(carry_in)

        return result_list.get_head()



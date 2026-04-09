#!/bin/python3

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
    @staticmethod
    def from_list(lst: list) -> "ListNode":
        current = head = None
        for item in lst:
            if not head:
                current = head = ListNode(item)
            else:
                current.next = ListNode(item)
                current = current.next

        return head
    
    def __str__(self):
        return str(self.val) + " -> "+ str(self.next)
    def __repr__(self):
        print(self.val, self.next)


class Solution:

    def __init__(self):
        self.carry:int = 0
        self.result_head: Optional[ListNode] = None
        self.result_current: Optional[ListNode] = self.result_head

    def addTwoNumbers(self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        current_1 = l1
        current_2 = l2
        while current_1 != None or current_2 != None:
            if not self.result_head:
                self.result_current = self.result_head = ListNode()
            else:
                self.result_current.next = ListNode()
                self.result_current = self.result_current.next

            current_1, current_2 = self.add_one_digit(current_1, current_2)

        if self.carry:
            self.result_current.next = ListNode(self.carry)

        return self.result_head

    def add_one_digit(self,
        current_1: Optional[ListNode],
        current_2: Optional[ListNode]
    ) -> tuple[Optional[ListNode], Optional[ListNode]]:

        item1 = current_1.val if current_1 else 0
        item2 = current_2.val if current_2 else 0

        # print(item1, item2, self.carry)

        if item1 + item2 + self.carry > 9:
            self.result_current.val = item1 + item2 + self.carry - 10
            self.carry = 1
        else:
            self.result_current.val = item1 + item2 + self.carry
            self.carry = 0

        current_1 = current_1.next if current_1 else None
        current_2 = current_2.next if current_2 else None

        # print(self.result_head)
        return current_1, current_2


solution = Solution()

# print(ListNode.from_list([2,4,3]))
# print(ListNode.from_list([5,6,4,7]))

print(solution.addTwoNumbers(
    ListNode.from_list([2,4,3]),
    ListNode.from_list([5,6,4])
))

print(solution.addTwoNumbers(
    ListNode.from_list([0]),
    ListNode.from_list([0])
))

print(solution.addTwoNumbers(
    ListNode.from_list([9,9,9,9,9,9,9]),
    ListNode.from_list([9,9,9,9])
))

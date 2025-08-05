# Definition for singly-linked list.
from typing import Optional

'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

O(max(n,m)) time complexity
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def main(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

    result = ListNode()
    temp = result

    carry = 0
    while l1 != None and l2 != None:
        digit = l1.val + l2.val + carry

        if digit > 9:
            digit = digit - 10
            carry = 1
        else: 
            carry = 0
        
        l1 = l1.next
        l2 = l2.next

        temp.val = digit
        if l1 or l2:
            temp.next = ListNode()
            temp = temp.next

    if l1 != None:
        while l1 != None:
            digit = l1.val + carry

            if digit > 9:
                digit = digit - 10
                carry = 1
            else: 
                carry = 0

            l1 = l1.next

            temp.val = digit
            if l1:
                temp.next = ListNode()
                temp = temp.next


    if l2 != None:
        while l2 != None:
            digit = l2.val + carry

            if digit > 9:
                digit = digit - 10
                carry = 1
            else: 
                carry = 0

            l2 = l2.next

            temp.val = digit
            if l2:
                temp.next = ListNode()
                temp = temp.next


    if carry == 1:
        temp.next = ListNode()
        temp = temp.next
        temp.val = 1



    return result

def to_list(node: Optional[ListNode]) -> list:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    # l1 = [2,4,3], 
    # l2 = [5,6,4]
    l1 = ListNode(2,ListNode(4,ListNode(3)))
    l2 = ListNode(5,ListNode(6,ListNode(4)))
    print(to_list(main(l1, l2)))
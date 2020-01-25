'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        strNum = str(self.getIntVal(l1) + self.getIntVal(l2))
        i = 0
        result = None

        while i < len(strNum):
            result = self.push(result, int(strNum[i]))
            i += 1 

        return result

    def getIntVal(self, node: ListNode, result = '') -> int:
        return self.getIntVal(node.next, result + str(node.val)) if node else int(result[::-1])

    def push(self, head: ListNode, data):
        node = ListNode(data)
        node.next = head
        return node
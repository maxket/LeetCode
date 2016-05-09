# This question is going to add two linked lists and return the result in another linked list
# Should consider:
#	1. order(reverse or not)
#	2. different length for two linked list
#	3. to remember the carry

# Just traverse the two linked lists one by one until one linked list end, time complexity is O(n)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if (l1 == None):
            return l2
        
        if (l2 == None):
            return l1
        
        carry = 0
        dummy_node = ListNode(-1)
        head = dummy_node
        
        while (l1 != None or l2 != None or carry != 0):
            if (l1 != None):
                carry += l1.val
                l1 = l1.next
            if (l2 != None):
                carry += l2.val
                l2 = l2.next
            head.next = ListNode(carry % 10)
            carry = carry / 10
            head = head.next
        
        return dummy_node.next

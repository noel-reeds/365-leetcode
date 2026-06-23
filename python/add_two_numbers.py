# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not l1 or not l2:
            return None
        if len(l2) > len(l1):
            for df in range(len(l2) - len(l1)):
                l1.append(0)
        elif len(l1) > len(l2):
            for df in range(len(l1) - len(l2)):
                l2.append(0)
        

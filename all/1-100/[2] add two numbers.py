class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1. Standard Iterative Approach (Optimal)
# Idea: Simulate digit-by-digit addition using a loop, tracking carry.
# Time Complexity: O(max(n, m)) | Space Complexity: O(max(n, m)) 
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()
    current = dummy
    carry = 0
    
    while l1 or l2 or carry:
        # Get values from current nodes (or 0 if list is exhausted)
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Compute total and carry
        total = val1 + val2 + carry
        carry = total // 10
        current.next = ListNode(total % 10)
        current = current.next
        
        # Move to next nodes if available
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next
    
    return dummy.next

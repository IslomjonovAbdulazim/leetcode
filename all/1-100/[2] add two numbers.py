

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

# 2. Integer Conversion Approach (Python-Specific)
# Idea: Convert linked lists to integers, sum them, then convert back to a linked list.
# Caveat: Works in Python due to arbitrary-precision integers but may overflow in other languages.
# Time Complexity: O(max(n, m)) | Space Complexity: O(max(n, m))
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    def list_to_num(node: ListNode) -> int:
        num = 0
        power = 0
        while node:
            num += node.val * (10 ** power)
            power += 1
            node = node.next
        return num
    
    total = list_to_num(l1) + list_to_num(l2)
    
    # Handle sum = 0 edge case
    if total == 0:
        return ListNode(0)
    
    # Convert total back to reversed linked list
    dummy = ListNode()
    current = dummy
    while total > 0:
        current.next = ListNode(total % 10)
        current = current.next
        total //= 10
    
    return dummy.next

# 3. Recursive Approach (For Completeness)
# Idea: Recursively compute digits and carry.
# Caveat: Risk of stack overflow for very long lists.
# Time Complexity: O(max(n, m)) | Space Complexity: O(max(n, m))
def addTwoNumbers(l1: ListNode, l2: ListNode, carry=0) -> ListNode:
    # Base case: stop when all lists and carry are exhausted
    if not l1 and not l2 and carry == 0:
        return None
    
    # Compute current sum and new carry
    val1 = l1.val if l1 else 0
    val2 = l2.val if l2 else 0
    total = val1 + val2 + carry
    new_carry = total // 10
    
    # Create new node
    node = ListNode(total % 10)
    
    # Prepare next nodes for recursion
    next1 = l1.next if l1 else None
    next2 = l2.next if l2 else None
    
    # Recursive call to build the rest of the list
    node.next = addTwoNumbers(next1, next2, new_carry)
    
    return node

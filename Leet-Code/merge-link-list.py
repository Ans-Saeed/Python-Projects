class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:
    # Create a dummy node to hold the head of the new list
    dummy = ListNode(0)
    # Pointer to the current node in the new list
    cur = dummy
    # Traverse both lists simultaneously
    while l1 and l2:
        # If the value in list1 is smaller, add it to the new list
        if l1.val <= l2.val:
            cur.next = l1
            l1 = l1.next
        # Otherwise, add the value in list2 to the new list
        else:
            cur.next = l2
            l2 = l2.next
        # Move the current pointer to the last node in the new list
        cur = cur.next
    # Attach the rest of the remaining list to the new list
    cur.next = l1 or l2
    # Return the head of the new list (excluding the dummy node)
    return dummy.next



l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(3, ListNode(4)))
merged = mergeTwoLists(l1, l2)
# The merged list should be: 1 -> 1 -> 2 -> 3 -> 4 -> 4

# Add two numbers represented as Linked Lists.

# Example 1:
# Input: num1 = 243, num2 = 564
# Output:sum = 807; L = [7,0,8]

# Explanation: Since the digits are stored in reverse order, reverse the numbers first to get the or original number and then add them as → 342 + 465 = 807. 

# Example 2:
# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: Result: [8,9,9,9,0,0,0,1]

# Explanation: Since the digits are stored in reverse order, reverse the numbers first to get the original number and then add them as → 9999999 + 9999 = 8999001. Refer to the image below.

# Create a dummy node that will act as the starting point of the new linked list.
# Create a temporary pointer and set it to the dummy node.
# Start with a carry value of 0.
# Loop through both linked lists until you reach the end of both, or until there is no carry left.
# At each step, add the values of the current nodes and the carry.
# Update the carry by dividing the total by 10.
# Create a new node with the last digit of the total (total % 10) and attach it to the next of the temporary pointer, then move the temporary pointer forward.
# Move both list pointers to their next nodes.
# After the loop ends, return the next node of the dummy (this is the head of the result list).
# The dummy node is used to make the code easier. Without it, extra conditions would be needed to handle the first node.

# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        # Value stored in the node
        self.val = val    
        # Pointer to the next node
        self.next = next  

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy node to simplify handling the result list
        dummy = ListNode()
        # Pointer to the current node in the result list
        temp = dummy  
        # Carry from the previous digit addition
        carry = 0     

        # Loop until both lists are fully traversed and no carry remains
        while (l1 is not None or l2 is not None) or carry:
            sum_val = 0  # Holds the sum of current digits and carry

            # Add l1's value to sum if l1 exists
            if l1 is not None:
                sum_val += l1.val
                l1 = l1.next

            # Add l2's value to sum if l2 exists
            if l2 is not None:
                sum_val += l2.val
                l2 = l2.next

            # Add any carry from the previous step
            sum_val += carry

            # Update carry for the next addition
            carry = sum_val // 10

            # Create a new node with the digit value (sum % 10)
            node = ListNode(sum_val % 10)
            # Append the new node to the result list
            temp.next = node  
            # Move temp forward
            temp = temp.next  

        # Return the result list, skipping the dummy node
        return dummy.next
def create_list(arr):
    head = ListNode(arr[0])
    temp = head
    for i in arr[1:]:
        temp.next = ListNode(i)
        temp = temp.next
    return head

def print_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next

if __name__ == "__main__":
    num1 = [2, 4, 3]  # represents 342
    num2 = [5, 6, 4]  # represents 465
    l1 = create_list(num1)
    l2 = create_list(num2)

    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)
    print_list(result)  # Output: 7 -> 0 -> 8

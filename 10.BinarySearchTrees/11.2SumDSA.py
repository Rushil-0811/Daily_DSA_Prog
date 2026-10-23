# In the Two Sum IV - Input is a BST problem, you are given the root node of a binary search tree and an integer target k. Your task is to determine if there are any two distinct nodes within the tree whose values add up exactly to the target k. Return true if such a pair exists, and false if no such pair can be found anywhere in the tree.

# Example 1
# Input: root = [5, 3, 6, 2, 4, null, 7], k = 9

# Output: true

# Explanation: The tree contains the values 5, 3, 6, 2, 4, and 7. If we take the node with value 3 and the node with value 6, their sum is exactly 9. Because a valid pair exists, the result is true.

# Example 2
# Input: root = [5, 3, 6, 2, 4, null, 7], k = 28

# Output: false

# Explanation: The tree contains the same values. However, even if we add the two absolute largest numbers in the tree together (6 + 7), the maximum possible sum is 13. It is physically impossible to reach the target of 28, so the result is false.

# Practice it by yourself before moving onto the solution
# Try now
# Brute Force Approach
# Finding two matching numbers is much easier when all the numbers are lined up in order from smallest to largest. A binary search tree is naturally sorted, but the numbers are spread out across hierarchical branches. By performing a standard inorder traversal, we can extract every single number and place it into a flat, perfectly sorted list. Once we have this sorted list, we can place one pointer at the smallest number and another pointer at the largest number. If their sum is too big, we move the larger pointer down. If their sum is too small, we move the smaller pointer up. If you want to understand this in detail, check our guide on the Two Pointer Technique.

# Algorithm
# Create an empty dynamic array to hold our extracted numbers.

# Write a recursive helper function to perform an inorder traversal (visit left child, visit root, visit right child) and push each value into the array.

# Call the helper function on the root of the tree.

# Set a left pointer to the first index of the array (0) and a right pointer to the last index of the array.

# Start a loop that continues as long as left is strictly less than right.

# Calculate the sum of the numbers at the left and right pointers.

# If the sum exactly matches the target k, return true immediately.

# If the sum is strictly less than the target, increment the left pointer to increase the total sum.

# If the sum is strictly greater than the target, decrement the right pointer to decrease the total sum.

# If the loop breaks without finding a match, return false.

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Helper function to extract tree values in strictly increasing order
    def inorder(self, root, nums):
        # Base case: stop if the node is empty
        if root is None:
            return
            
        # Traverse the left side completely
        self.inorder(root.left, nums)
        # Store the current node's value
        nums.append(root.val)
        # Traverse the right side completely
        self.inorder(root.right, nums)

    # Main function to find the target sum using a list and two pointers
    def findTarget(self, root, k):
        nums = []
        # Flatten the BST into a sorted list
        self.inorder(root, nums)
        
        # Initialize pointers at the extreme ends of the list
        left = 0
        right = len(nums) - 1
        
        # Loop to check pairs until the pointers cross
        while left < right:
            currentSum = nums[left] + nums[right]
            
            # If the exact target is found, return true
            if currentSum == k:
                return True
                
            # If the sum is too small, move to a larger number on the left
            if currentSum < k:
                left += 1
            # If the sum is too large, move to a smaller number on the right
            else:
                right -= 1
                
        # No valid pairs exist
        return False

# Driver code starts here
if __name__ == "__main__":
    # Construct the sample tree: [5, 3, 6, 2, 4, None, 7]
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    
    obj = Solution()
    k = 9
    
    # Check if the target exists
    result = obj.findTarget(root, k)
    print("true" if result else "false")

# Optimal Approach
# Extracting everything into an array takes unnecessary RAM. If the tree contains millions of elements, we create an array of millions of elements, even if the target numbers are the very first two numbers we check. We can drastically improve our memory usage by using customized iterators that walk through the tree one step at a time, calculating the sums on the fly. If you want to understand this in detail, check our guide on the Binary Search Tree Iterator.

# Consider two explorers navigating a mountain range. One explorer starts at the absolute lowest valley and only walks upward. The second explorer starts at the highest peak and only walks downward. They pause at every checkpoint and communicate their combined altitude via radio. If the total altitude is too low, the bottom explorer climbs one checkpoint higher. If the total is too high, the top explorer climbs one checkpoint lower. They use a breadcrumb trail (a stack) to remember their paths without mapping the entire mountain range at once.

# Algorithm
# Create a custom BSTIterator class. It should accept a boolean flag reverse. If reverse is false, it behaves like a normal in-order iterator (yielding smallest to largest). If reverse is true, it behaves as a reverse in-order iterator (yielding largest to smallest).

# Inside the main solution, instantiate two iterators: leftIter (normal) and rightIter (reverse).

# Retrieve the first elements from both iterators: i from leftIter and j from rightIter.

# Loop while i is strictly less than j.

# Check the sum of i and j. If it matches k, return true.

# If the sum is strictly less than k, move the left explorer forward by calling next() on leftIter and updating i.

# If the sum is strictly greater than k, move the right explorer backward by calling next() on rightIter and updating j.

# Return false if the iterators cross paths without finding a match.

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Custom iterator class that can traverse the tree from smallest to largest
# or from largest to smallest, depending on the initialization flag
class BSTIterator:
    # Constructor initializes the appropriate path
    def __init__(self, root, isReverse):
        self.st = []
        self.reverse = isReverse
        self._pushAll(root)
        
    # Helper function to push all boundary nodes onto the stack
    def _pushAll(self, node):
        while node is not None:
            self.st.append(node)
            # If traversing backwards, load right children. Otherwise, load left children.
            if self.reverse:
                node = node.right
            else:
                node = node.left

    # Retrieves the next target element in the sequence
    def next(self):
        topNode = self.st.pop()
        
        # If traversing backwards, look left for the next smaller element
        if self.reverse:
            self._pushAll(topNode.left)
        # If traversing forwards, look right for the next larger element
        else:
            self._pushAll(topNode.right)
            
        return topNode.val

class Solution:
    # Main function linking the forward and reverse iterators
    # to simulate the optimal two-pointer array technique
    def findTarget(self, root, k):
        # Guard clause for empty trees
        if root is None:
            return False
            
        # Initialize one iterator at the minimum and one at the maximum
        leftIter = BSTIterator(root, False)
        rightIter = BSTIterator(root, True)
        
        i = leftIter.next()
        j = rightIter.next()
        
        # Loop until the iterators cross each other
        while i < j:
            currentSum = i + j
            
            # The exact sum is found
            if currentSum == k:
                return True
                
            # Sum is too small, advance the left iterator
            if currentSum < k:
                i = leftIter.next()
            # Sum is too large, advance the right iterator
            else:
                j = rightIter.next()
                
        return False

# Driver code starts here
if __name__ == "__main__":
    # Construct the sample tree: [5, 3, 6, 2, 4, None, 7]
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)
    
    obj = Solution()
    k = 9
    
    # Check if the target exists
    result = obj.findTarget(root, k)
    print("true" if result else "false")
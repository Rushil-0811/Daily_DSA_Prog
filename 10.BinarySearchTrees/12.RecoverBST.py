# The Recover Binary Search Tree problem provides you with the root of a binary search tree where exactly two nodes have had their values swapped by mistake. Your task is to identify these two anomalies and swap their values back to restore the tree's strict sorting rules. You must modify the values in place without altering the physical structure of the tree.

# Example 1
# Input: root = [1,3,null,null,2]

# Output: [3, 1, null, null, 2]

# Explanation: The sorted sequence of this tree is broken because 3 appears as a left child, which is larger than the root 1. Swapping the values 1 and 3 perfectly restores the standard left-less-than-root property.

# Example 2
# Input: root = [3,1,4,null,null,2]

# Output: [2, 1, 4, null, null, 3]

# Explanation: During a traversal, the value 2 appears on the right side of 3, which violates the rule that right-side children must be strictly larger. Swapping 2 and 3 corrects the entire tree's ordering.

# Brute Force Approach
# Think of a school assembly line where students are arranged perfectly by height. If exactly two students secretly swap places, the line is no longer perfectly sorted. If we take a photograph of the current messy line, sort the students by height on paper, and then compare our sorted list to the actual line, we can easily spot who moved and tell them to swap back.

# In a binary search tree, reading the nodes from left to root to right is called an inorder traversal. This traversal maps perfectly to reading a sorted list. If we extract all the node values, sort them, and put them back in the tree one by one, we will fix the mistakenly swapped values. If you want to understand this in detail, check our guide on Inorder Traversal.

# Algorithm
# Traverse the binary tree using inorder traversal.

# Store every node value you visit into a list. This list represents the current broken order.

# Sort the list. Now you have the completely correct order of values.

# Traverse the binary tree a second time using inorder traversal.

# During the second traversal, replace the value of the current node with the correct value from your sorted list, moving step-by-step through the list.

# The termination condition for both traversals is when the current node becomes null, meaning we have reached the end of a branch.
    

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Performs inorder traversal to extract tree values
    def collectValues(self, root, values):
        if not root:
            return
            
        self.collectValues(root.left, values)
        values.append(root.val)
        self.collectValues(root.right, values)

    # Inorder traversal to assign the correct sorted values back
    def replaceValues(self, root, values, index_tracker):
        if not root:
            return
            
        self.replaceValues(root.left, values, index_tracker)
        # Re-assign node value and move to the next item in the sorted list
        root.val = values[index_tracker[0]]
        index_tracker[0] += 1
        self.replaceValues(root.right, values, index_tracker)

    # Recovers the tree by extracting, sorting, and replacing
    def recoverTree(self, root):
        values = []
        self.collectValues(root, values)
        
        # Sorting restores the natural left-to-right order of the tree
        values.sort()
        
        # Using a list to hold the index allows it to be updated inside recursion
        index_tracker = [0]
        self.replaceValues(root, values, index_tracker)

# Helper function to print inorder traversal
def print_inorder(node):
    if not node:
        return
    print_inorder(node.left)
    print(node.val, end=" ")
    print_inorder(node.right)

# Driver code starts here
if __name__ == "__main__":
    # Create the faulty tree [1,3,null,null,2]
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.right = TreeNode(2)

    obj = Solution()
    obj.recoverTree(root)

    print("Recovered tree (Inorder traversal):", end=" ")
    print_inorder(root)
    print()

# Complexity Analysis
# Time Complexity: O(N x log N), N is the number of nodes, the sorting step takes N x logN time for N extracted elements.

# Space Complexity: O(N), N is the number of nodes, storing the values in an array requires extra memory proportional to the tree size.

# Optimal Approach
# The previous approach is inefficient because it requires extra memory to store an array of size N, and extra time to sort it. Since we know the tree is almost perfectly sorted except for exactly two swapped nodes, we don't need to rebuild the entire sequence. We can just keep a watchful eye on the order as we traverse the tree and immediately flag any values that break the rules.

# Let us return to the real-life example of students lined up by height. Instead of taking a photo and sorting it, an inspector simply walks down the line from start to finish. The inspector constantly compares the current student they are looking at with the previous student they just passed.

# If the inspector sees a taller student standing right before a shorter student, they know a mistake happened. They remember who was out of place. By tracking the previous person they saw, they can walk the whole line just once, catch the two people who ruined the order, and tell them to swap.

# We can do exactly this in our tree. By saving a pointer to the previous node we visited, we can spot where the sorted order drops. The variables first, middle, and last will help us remember exactly which nodes caused these drops.

# Algorithm
# Create four variables: prev to track the node we just visited, and first, middle, last to track the nodes that are out of place.

# Perform an inorder traversal of the tree. The termination condition is when the root becomes null.

# At each node, check if the value of the prev node is strictly greater than the current node. If it is, the sorted order is broken.

# If this is the very first time the order is broken, save the prev node as first, and the current node as middle.

# If the order breaks a second time later in the traversal, save the current node as last.

# Once the traversal finishes, check if we found a last node. If so, swap the values of the first node and the last node.

# If we only broke the order once, it means the swapped nodes were right next to each other in the sequence. In this case, just swap the first node and the middle node.

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Performs inorder traversal to extract tree values
    def collectValues(self, root, values):
        if not root:
            return
            
        self.collectValues(root.left, values)
        values.append(root.val)
        self.collectValues(root.right, values)

    # Inorder traversal to assign the correct sorted values back
    def replaceValues(self, root, values, index_tracker):
        if not root:
            return
            
        self.replaceValues(root.left, values, index_tracker)
        # Re-assign node value and move to the next item in the sorted list
        root.val = values[index_tracker[0]]
        index_tracker[0] += 1
        self.replaceValues(root.right, values, index_tracker)

    # Recovers the tree by extracting, sorting, and replacing
    def recoverTree(self, root):
        values = []
        self.collectValues(root, values)
        
        # Sorting restores the natural left-to-right order of the tree
        values.sort()
        
        # Using a list to hold the index allows it to be updated inside recursion
        index_tracker = [0]
        self.replaceValues(root, values, index_tracker)

# Helper function to print inorder traversal of the tree
def print_inorder(root):
    if not root:
        return
    print_inorder(root.left)
    print(root.val, end=" ")
    print_inorder(root.right)

# Driver code starts here
if __name__ == "__main__":
    # Create the faulty tree [1,3,null,null,2]
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.left.right = TreeNode(2)

    obj = Solution()
    obj.recoverTree(root)

    # Print the full tree traversal
    print("Recovered tree (Inorder traversal):", end=" ")
    print_inorder(root)
    print()
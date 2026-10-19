# You are given the root node of a binary search tree and an integer K. Your task is to find the Kth largest/smallest element in Binary Search Tree. You need to return an array containing two integers, where the first integer is the Kth smallest value and the second integer is the Kth largest value from all the nodes present in the tree.

# Example 1
# Input: Root of tree with nodes [5, 3, 6, 2, 4, null, null, 1], K = 3

# Output: [3, 4]

# Explanation: The sorted values of the tree are [1, 2, 3, 4, 5, 6]. The 3rd smallest value is 3 from the beginning, and the 3rd largest value is 4 from the end.

# Example 2
# Input: Root of tree with nodes [2, 1, 3], K = 2

# Output: [2, 2]

# Explanation: The sorted values are [1, 2, 3]. The 2nd smallest value is 2, and the 2nd largest value is also 2.

# Brute Force Approach
# Think of organizing a messy stack of test papers based on student scores. If we lay out all the papers in increasing order of their marks, finding the Kth lowest or Kth highest score simply requires picking the Kthpaper from the start or the end of the line.

# A binary search tree has a special property where traversing it in an Inorder manner (visiting the left child, then the root, then the right child) yields all the node values in strictly increasing order. By doing this traversal and writing down every value in an array, we get a fully sorted list of elements. From this sorted list, the Kthsmallest element is found at index K minus 1. The Kth largest element is found by counting K positions backward from the end of the list.

# Algorithm
# Create an empty array to store the node values.

# Start an inorder traversal from the root node to get the node values in sorted order.

# Recursively visit the left subtree first so smaller values gets added first.

# Append the current node's value to the array, all smaller values than root added now root.

# Recursively visit the right subtree, now larger values than root are added.

# Once the traversal is complete and the array is filled, find the Kth smallest element at index K minus 1.

# Find the Kth largest element at the index equal to the total size of the array minus K.

# Return these two values in a new array.

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # Function to collect all tree values in sorted order
    def inorder(self, root, values):
        # Stop execution if the current node does not exist
        if not root:
            return
        
        # Traverse down the left side
        self.inorder(root.left, values)
        
        # Save the value of the node
        values.append(root.val)
        
        # Traverse down the right side
        self.inorder(root.right, values)

    # Main logic to extract the Kth elements
    def findKthElements(self, root, k):
        values = []
        
        # Execute the inorder traversal
        self.inorder(root, values)
        
        n = len(values)
        
        # Fetch the Kth smallest and largest using indexing
        kth_smallest = values[k - 1]
        kth_largest = values[n - k]
        
        return [kth_smallest, kth_largest]

# Driver code starts here
if __name__ == "__main__":
    # Setting up the tree nodes manually
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    
    obj = Solution()
    k = 2
    
    # Passing the tree to the solution class
    result = obj.findKthElements(root, k)
    
    # Printing the final output
    print(f"Smallest: {result[0]}, Largest: {result[1]}")

# Optimal Approach
# The previous approach requires storing every single element in a list, which takes up a lot of extra space. If a tree has millions of nodes, storing all of them just to find the second or third element is inefficient. We can solve this by skipping the storage entirely.

# Instead of making all students stand in a line and taking up a massive hallway, we just stand at the door. As students walk out in increasing order of their marks, we keep a tally on a notepad. When the Kth student walks out, we write down their name and we can stop counting.

# For the binary search tree, we can traverse it in the standard inorder way (Left, Root, Right) to count the smallest elements. When our counter reaches K, we have found the Kth smallest element. To find the Kth largest element, we can do the exact same thing but in reverse. By traversing Right, Root, Left, we process the elements in decreasing order. When the counter reaches K during this reverse traversal, we have found the Kth largest element.

# If you want to understand this in detail, check our guide on Tree Traversals.

# Algorithm
# Create two variables to keep track of our count, one for the smallest and one for the largest.

# Create two variables to store the final answers.

# Write a recursive function for the Kth smallest element that visits the left node, increments the counter, checks if the counter equals K, stores the value if true, and then visits the right node.

# Write a second recursive function for the Kth largest element that visits the right node first, increments the counter, checks if the counter equals K, stores the value if true, and then visits the left node.

# Call both functions sequentially.

# Return the stored answers in an array.

# Definition for a binary tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.countSmallest = 0
        self.countLargest = 0
        self.kthSmallestVal = -1
        self.kthLargestVal = -1

    # Standard tree traversal keeping count
    def __findSmallest(self, root, k):
        if not root or self.countSmallest >= k:
            return
        
        self.__findSmallest(root.left, k)
        
        # Check if the required count is met
        self.countSmallest += 1
        if self.countSmallest == k:
            self.kthSmallestVal = root.val
            return
            
        self.__findSmallest(root.right, k)

    # Reverse tree traversal keeping count
    def __findLargest(self, root, k):
        if not root or self.countLargest >= k:
            return
        
        self.__findLargest(root.right, k)
        
        # Check if the required count is met
        self.countLargest += 1
        if self.countLargest == k:
            self.kthLargestVal = root.val
            return
            
        self.__findLargest(root.left, k)

    # Function to coordinate tracking logic
    def findKthElements(self, root, k):
        self.__findSmallest(root, k)
        self.__findLargest(root, k)
        
        return [self.kthSmallestVal, self.kthLargestVal]

# Driver code starts here
if __name__ == "__main__":
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    
    obj = Solution()
    k = 3
    
    result = obj.findKthElements(root, k)
    
    print(f"Smallest: {result[0]}, Largest: {result[1]}")
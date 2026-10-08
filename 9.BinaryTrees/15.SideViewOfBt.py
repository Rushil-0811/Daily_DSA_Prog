# Left and Right View of a Binary Tree
# The left view of a binary tree contains the nodes visible when the tree is observed from its left side.

# The right view contains the nodes visible when the tree is observed from its right side.

# At every level:

# The first node from the left belongs to the left view.

# The first node from the right belongs to the right view.

# Both views contain exactly one node from every non-empty level and are returned from top to bottom.

# Consider a binary tree with the following relationships:

# Node 1 is the root.

# Nodes 2 and 3 are the children of 1.

# Node 4 is the right child of 2.

# Node 5 is the left child of 3.

# Node 6 is the right child of 4.

# The nodes at each level are:

# herefore:

# Left View = [1, 2, 4, 6]

# Right View = [1, 3, 5, 6]

# Notice that node 4 belongs to the left view even though it is a right child. Similarly, a right-view node does not always need to be connected through right-child edges.

# Given the root of a binary tree, determine:

# The left view of the tree

# The right view of the tree

# The left view should contain the leftmost node at every level, while the right view should contain the rightmost node at every level.

# Return the nodes in top-to-bottom order.

# If the tree is empty, both views are empty.

# Examples
# Example 1
# Using the tree described above:

# Left View = [1, 2, 4, 6]

# Right View = [1, 3, 5, 6]

# Example 2
# Consider a tree containing only one node:

# Root = 10

# The root is visible from both sides.

# Left View = [10]

# Right View = [10]

# Important Observation
# The left and right views are based on the extreme node at each level.

# They are not necessarily:

# A path containing only left children

# A path containing only right children

# The complete left or right boundary of the tree

# For example, if a node has no left child, its right child may still become the leftmost visible node at a deeper level.

# The problem can therefore be reduced to:

# Find the first and last node at every level.

# This observation leads naturally to a BFS solution. The same information can also be collected using DFS by controlling the subtree visitation order.

# Approach 1
# Intuition
# Breadth-First Search processes the tree one level at a time.

# For every level:

# The first node processed is the leftmost node.

# The last node processed is the rightmost node.

# By recording these two nodes, both views can be generated during the same level-order traversal.

# A queue maintains the nodes waiting to be processed. Before processing a level, record the current queue size so that only the nodes belonging to that level are considered.

# Algorithm
# Return empty views if the root is NULL; otherwise, place the root in a queue.

# Record the queue size before each level because it equals the number of nodes currently present at that level.

# Process exactly those nodes from left to right while adding their existing children to the queue.

# Add the first processed node of the level to the left view.

# Add the last processed node of the level to the right view.

# Continue until the queue becomes empty, then return both views.

# Dry Run
# Consider the example tree.

# Initial state:

# Queue = [1]

# Left View = []

# Right View = []

# Level 0
# Current queue:

# [1]

# The level contains only node 1.

# First node: 1

# Last node: 1

# Update:

# Left View = [1]

# Right View = [1]

# Add children 2 and 3:

# Queue = [2, 3]

# Level 1
# Current queue:

# [2, 3]

# First node: 2

# Last node: 3

# Update:

# Left View = [1, 2]

# Right View = [1, 3]

# Node 2 adds child 4, and node 3 adds child 5:

# Queue = [4, 5]

# Level 2
# Current queue:

# [4, 5]

# First node: 4

# Last node: 5

# Update:

# Left View = [1, 2, 4]

# Right View = [1, 3, 5]

# Node 4 adds child 6:

# Queue = [6]

# Level 3
# Current queue:

# [6]

# The level contains only node 6.

# First node: 6

# Last node: 6

# Update:

# Left View = [1, 2, 4, 6]

# Right View = [1, 3, 5, 6]

# The queue becomes empty, so traversal is complete.

# Why Does the BFS Approach Work?
# BFS processes all nodes at depth D before moving to depth D + 1.

# Since children are inserted from left to right, the nodes of every level are removed from the queue in left-to-right order.

# Therefore:

# The first node processed at a level is its leftmost node.

# The last node processed at a level is its rightmost node.

# Selecting these nodes for every level produces the left and right views.

# Complexity Analysis
# Every node is inserted into and removed from the queue once.

# Time Complexity: O(N)

# The queue may contain all nodes from the widest level.

# Auxiliary Space Complexity: O(W)

# where W is the maximum width of the tree.

# The returned views contain one value per level. For a tree of height H, their combined output space is:

# O(H)

# Output space is not included in auxiliary space unless stated otherwise.

# Approach 2
# Intuition
# DFS can identify view nodes by tracking the current depth.

# The view list initially contains no value for an unexplored depth. Therefore, when DFS reaches a depth for the first time, the current node is recorded.

# The subtree visitation order determines which node is encountered first:

# For the left view, visit the left subtree before the right subtree.

# For the right view, visit the right subtree before the left subtree.

# This ensures that the first node reached at every depth is the node visible from the required side.

# DFS for the Left View
# Use the traversal order:

# Root → Left → Right

# When visiting a node at depth D:

# If the view already contains a value for depth D, another node at that level was reached earlier.

# If the view size equals D, this is the first node reached at that depth, so add it to the left view.

# Algorithm
# Begin DFS from the root at depth 0.

# Return when the current node is NULL because the branch has ended.

# Add the current node when the depth equals the current left-view size.

# Traverse the left subtree first so the leftmost node of each depth is encountered before other nodes.

# Traverse the right subtree afterward to process levels not reached through the left subtree.

# Continue until every reachable node has been examined.

# For the example tree:

# Left View = [1, 2, 4, 6]

# DFS for the Right View
# Use the traversal order:

# Root → Right → Left

# The depth condition remains the same, but the right subtree is explored first.

# Algorithm
# Begin DFS from the root at depth 0.

# Return when the current node is NULL.

# Add the current node when the depth equals the current right-view size.

# Traverse the right subtree first so the rightmost node of each depth is encountered before other nodes.

# Traverse the left subtree afterward to reach levels missing from the right subtree.

# Continue until all nodes have been examined.

# For the example tree:

# Right View = [1, 3, 5, 6]DFS Dry Run for the Left View
# Start with:

# Left View = []

# Visit Node 1 at Depth 0
# Depth = Left View Size = 0

# Add 1:

# Left View = [1]

# Visit Node 2 at Depth 1
# Depth = Left View Size = 1

# Add 2:

# Left View = [1, 2]

# Visit Node 4 at Depth 2
# Depth = Left View Size = 2

# Add 4:

# Left View = [1, 2, 4]

# Visit Node 6 at Depth 3
# Depth = Left View Size = 3

# Add 6:

# Left View = [1, 2, 4, 6]

# When DFS later reaches nodes 3 and 5, their depths already have recorded values, so they are not added.

# DFS Dry Run for the Right View
# Start with:

# Right View = []

# Visit Node 1 at Depth 0
# Add 1:

# Right View = [1]

# Visit Node 3 at Depth 1
# Add 3:

# Right View = [1, 3]

# Visit Node 5 at Depth 2
# Add 5:

# Right View = [1, 3, 5]

# The right-first traversal later enters the left subtree and eventually reaches node 6 at depth 3.

# Since no value has been recorded for that depth, add 6:

# Right View = [1, 3, 5, 6]

# This demonstrates why the right view is not limited to nodes connected only through right-child edges.

# Why Does the DFS Approach Work?
# For the left view, root-left-right traversal visits nodes at each depth from the left side before reaching nodes from the right side.

# Therefore, the first node reached at a new depth is the leftmost visible node.

# For the right view, reversing the subtree order makes the rightmost node the first one reached at every depth.

# The condition:

# depth == view size

# ensures that exactly one node is recorded for each level.

# Complexity Analysis
# Every node is visited once for each required DFS traversal.

# Even if the left and right views are generated using two separate traversals, the work is:

# 2N

# Ignoring the constant factor:

# Time Complexity: O(N)

# The recursion stack contains nodes along the active root-to-node path.

# Auxiliary Space Complexity: O(H)

# where H is the height of the tree.

# Balanced tree: O(log N)

# Skewed tree: O(N)

# The output space for each view is O(H).

# BFS and DFS Comparison
# BFS

# DFS

# Processes the tree level by level

# Explores one branch deeply before backtracking

# Records the first and last node of each level

# Records the first node reached at each depth

# Generates both views naturally in one traversal

# Uses a different subtree order for each view

# Uses O(W) queue space

# Uses O(H) recursion or stack space

# Avoids recursion-depth limits

# Usually has a shorter recursive explanation

# Useful when level information is also required

# Useful when only a side view is required

# Both approaches take O(N) time. The better space choice depends on the shape of the tree.

# Calculating Both Views in One Traversal
# Both views can be generated in one BFS by recording the first and last nodes of every level.

# They can also be generated in one left-to-right DFS:

# The first node encountered at a depth becomes the left-view node.

# Every later node encountered at the same depth replaces the current right-view value.

# After DFS completes, the last node visited at each depth is the rightmost node.

# The BFS method is usually easier to understand when both views are required together.

# Important Edge Cases
# Empty Tree
# Both views are empty:

# Left View = []

# Right View = []

# Single-Node Tree
# The root appears in both views.

# Skewed Tree
# Every level contains one node, so the left and right views are identical.

# Missing Left or Right Children
# The visible node may come from the opposite subtree. The algorithm must select the extreme node at each level rather than follow only one type of child reference.

# Duplicate Values
# Duplicate node values do not affect the traversal. Views depend on node positions, not value uniqueness.

# Common Mistakes
# Treating the left view as a path containing only left children.

# Treating the right view as a path containing only right children.

# Confusing side views with boundary traversal.

# Forgetting to handle an empty tree.

# Recording the changing queue size while processing a BFS level.

# Adding children in an order inconsistent with the intended left-to-right traversal.

# Recording every node instead of only the first or last node of a level.

# Using root-right-left DFS for the left view.

# Using root-left-right DFS for the right view when recording only the first node.

# Adding a DFS node without checking whether its depth is already represented.

# Counting output storage as auxiliary space without stating the convention.

# Assuming duplicate values make the view ambiguous

from collections import deque
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()

                # If it's the last node at this level, add it to result
                if i == level_size - 1:
                    result.append(node.val)

                # Push children into queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

class Solution:
    def dfs(self, node, depth, result):
        if not node:
            return

        # If this depth is being visited for the first time, add node
        if depth == len(result):
            result.append(node.val)

        # Visit right child first, then left child
        self.dfs(node.right, depth + 1, result)
        self.dfs(node.left, depth + 1, result)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.dfs(root, 0, result)
        return result
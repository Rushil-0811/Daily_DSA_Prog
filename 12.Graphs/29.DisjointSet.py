# Design a disjoint set, also called a union-find data structure, for N nodes numbered from 1 to N. Initially, every node belongs to a separate set.

# Support the following operations:

# DisjointSet(int n): Initialize a disjoint set containing n nodes.

# unionByRank(int u, int v): Merge the sets containing u and v using the rank heuristic.

# unionBySize(int u, int v): Merge the sets containing u and v using the size heuristic.

# find(int u, int v): Return true when u and v belong to the same set; otherwise, return false.

# The implementation also provides componentSizeOf(node) for retrieving the number of nodes in the set containing node.

# Example 1
# Input: N = 5, operations = [unionByRank(1,2), unionByRank(2,3), find(1,3), find(1,5)]

# Output: [true, false]

# Explanation: Rank-based merges place nodes 1, 2, and 3 in one set. Node 5 remains in a separate set.

# Example 2
# Input: N = 5, operations = [unionBySize(1,2), unionBySize(4,5), unionBySize(2,4), find(1,5), componentSizeOf(1)]

# Output: [true, 4]

# Explanation: Size-based merges create one set containing nodes 1, 2, 4, and 5.

# Approach 1
# A parent array represents every set as a rooted tree. Root nodes store the root index in the parent array. Path compression rewrites parent links directly to the representative during findParent, shortening future representative searches.

# Rank approximates tree height. unionByRank attaches the lower-rank root below the higher-rank root. Equal ranks allow either root to become the representative, followed by one rank increment.

# Algorithm
# Initialize parent[node]=node, rankValue[node]=0, and componentSize[node]=1 for every node.

# Run findParent(node) until reaching a root satisfying parent[node]=node.

# Assign the representative during recursive return, compressing every visited parent link.

# Run findParent for both nodes before unionByRank and stop after matching representatives.

# Attach the lower-rank root below the higher-rank root and update the surviving component size.

# Attach either root for equal ranks, increment the surviving rank, and update the surviving component size.

# Run find(u, v) through representative comparison.

class DisjointSet:
    # Initializes one independent set for every node.
    def __init__(self, n: int) -> None:
        self.parent = [0] * (n + 1)
        self.rankValue = [0] * (n + 1)

        # Make every node its own parent.
        for node in range(1, n + 1):
            self.parent[node] = node

    # Returns the representative using path compression.
    def findParent(self, node: int) -> int:
        # Base case: node is its own representative.
        if self.parent[node] == node:
            return node

        # Compress the path while finding the representative.
        self.parent[node] = self.findParent(self.parent[node])

        return self.parent[node]

    # Merges two sets using rank balancing.
    def unionByRank(self, u: int, v: int) -> None:
        rootU = self.findParent(u)
        rootV = self.findParent(v)

        # Same representative means both nodes are already connected.
        if rootU == rootV:
            return

        # Keep the higher-rank root as the parent.
        if self.rankValue[rootU] < self.rankValue[rootV]:
            rootU, rootV = rootV, rootU

        # Attach the lower-rank root to the higher-rank root.
        self.parent[rootV] = rootU

        # Increase rank only when both ranks are equal.
        if self.rankValue[rootU] == self.rankValue[rootV]:
            self.rankValue[rootU] += 1

    # Checks whether two nodes share one set.
    def find(self, u: int, v: int) -> bool:
        return self.findParent(u) == self.findParent(v)


# Driver code.
def main() -> None:
    dsu = DisjointSet(5)

    dsu.unionByRank(1, 2)
    dsu.unionByRank(2, 3)

    print(str(dsu.find(1, 3)).lower())
    print(str(dsu.find(1, 5)).lower())


if __name__ == "__main__":
    main()

# Approach 2
# The parent forest and path-compressed findParent operation remain unchanged. A component-size array stores the number of nodes belonging to each current representative.

# unionBySize attaches the smaller set below the larger set. The surviving representative receives the combined component size, allowing componentSizeOf(node) to return set cardinality directly.

# Algorithm
# Initialize parent[node]=node, rankValue[node]=0, and componentSize[node]=1 for every node.

# Run findParent(node) until reaching a root and compress the complete parent path during return.

# Run findParent for both nodes before unionBySize and stop after matching representatives.

# Compare both component sizes and swap representatives after locating a larger second component.

# Attach the smaller representative below the larger representative.

# Add the absorbed component size to the surviving representative and preserve a valid rank upper bound.

# Run find(u, v) through representative comparison and run componentSizeOf(node) through the representative size.

class DisjointSet:
    # Initializes one independent set for every node.
    def __init__(self, n: int) -> None:
        self.parent = [0] * (n + 1)
        self.componentSize = [1] * (n + 1)

        # Make every node its own parent.
        for node in range(1, n + 1):
            self.parent[node] = node

    # Returns the representative using path compression.
    def findParent(self, node: int) -> int:
        # Base case: node is its own representative.
        if self.parent[node] == node:
            return node

        # Compress the path while finding the representative.
        self.parent[node] = self.findParent(self.parent[node])

        return self.parent[node]

    # Merges two sets using component-size balancing.
    def unionBySize(self, u: int, v: int) -> None:
        rootU = self.findParent(u)
        rootV = self.findParent(v)

        # Same representative means both nodes are already connected.
        if rootU == rootV:
            return

        # Keep the larger component as the main parent.
        if self.componentSize[rootU] < self.componentSize[rootV]:
            rootU, rootV = rootV, rootU

        # Attach the smaller component to the larger component.
        self.parent[rootV] = rootU

        # Update the size of the merged component.
        self.componentSize[rootU] += self.componentSize[rootV]

    # Checks whether two nodes share one set.
    def find(self, u: int, v: int) -> bool:
        return self.findParent(u) == self.findParent(v)

    # Returns the number of nodes in one set.
    def componentSizeOf(self, node: int) -> int:
        return self.componentSize[self.findParent(node)]


# Driver code.
def main() -> None:
    dsu = DisjointSet(5)

    dsu.unionBySize(1, 2)
    dsu.unionBySize(4, 5)
    dsu.unionBySize(2, 4)

    print(str(dsu.find(1, 5)).lower())
    print(dsu.componentSizeOf(1))


if __name__ == "__main__":
    main()
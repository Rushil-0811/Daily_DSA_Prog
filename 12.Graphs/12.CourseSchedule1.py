# Given numCourses courses labeled from 0 to numCourses - 1 and a list of prerequisite pairs, return whether all courses can be finished.

# Each pair [course, prerequisite] means the prerequisite course must be completed before the course. Completion is possible only when the prerequisite graph has no directed cycle.

# Example 1
# Input: numCourses = 2, prerequisites = [[1,0]]

# Output: true

# Explanation: Course 0 can be completed before course 1.

# Example 2
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]

# Output: false

# Explanation: Course 0 and course 1 depend on each other, forming a cycle.

# Approach 1
# Each course becomes a vertex, and every pair creates a directed edge from prerequisite to dependent course. Depth First Search can detect whether a dependency chain returns to a course already active in the current DFS path.

# A visited array tracks courses already explored globally, while a path-visited array tracks courses in the active recursion chain. Reaching a path-visited course means circular dependency, so completing every course becomes impossible.

# Algorithm
# Build an adjacency list with a directed edge from each prerequisite course to its dependent course.

# Initialize visited and pathVisited arrays to track globally explored courses and courses in the current DFS path.

# Traverse every course to cover all disconnected components.

# Start DFS from each course that has not been visited.

# Mark the current course as visited and pathVisited.

# Run DFS for every unvisited dependent course and return false if any dependent course is already pathVisited.

# Remove the current course from pathVisited after all its dependencies are processed.

# Return true if no circular dependency is found.

from typing import List

class Solution:
    # Detects a cycle through the active DFS path.
    def hasCycle(self, course: int, visited: List[int], pathVisited: List[int], adj: List[List[int]]) -> bool:
        # Mark the course as visited.
        visited[course] = 1

        # Mark the course in the current DFS path.
        pathVisited[course] = 1

        # Explore all courses depending on the current course.
        for nextCourse in adj[course]:
            # Visit the next course if it is not visited.
            if not visited[nextCourse]:
                # If a cycle is found deeper, return true.
                if self.hasCycle(nextCourse, visited, pathVisited, adj):
                    return True

            # If next course is in the current path, a cycle exists.
            elif pathVisited[nextCourse]:
                return True

        # Remove course from the active DFS path.
        pathVisited[course] = 0

        # No cycle found from this course.
        return False

    # Checks if all courses can be finished.
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]

        # Build edge from prerequisite to dependent course.
        for pairValue in prerequisites:
            course = pairValue[0]
            prerequisite = pairValue[1]

            adj[prerequisite].append(course)

        visited = [0] * numCourses
        pathVisited = [0] * numCourses

        # Start DFS from every unvisited course.
        for course in range(numCourses):
            # Only unvisited courses can start a new DFS.
            if not visited[course]:
                # If a cycle exists, all courses cannot be finished.
                if self.hasCycle(course, visited, pathVisited, adj):
                    return False

        # No circular dependency exists.
        return True


# Driver code.
if __name__ == "__main__":
    numCourses = 2

    prerequisites = [
        [1, 0]
    ]

    sol = Solution()

    print(str(sol.canFinish(numCourses, prerequisites)).lower())


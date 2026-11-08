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

# Approach 2
# Kahn Algorithm treats courses with indegree 0 as immediately available because no prerequisites block them. Completing such a course removes outgoing dependency effect from dependent courses.

# If all courses can be processed through repeated zero-indegree removal, no cycle exists. If some courses never reach indegree 0, a circular dependency remains.

# Algorithm
# Build an adjacency list and an indegree array from all prerequisite pairs.

# Add every course with indegree = 0 to a queue.

# Initialize completed as 0.

# Pop a course from the queue and increase completed.

# Reduce the indegree of every dependent course.

# Add a dependent course to the queue when its indegree becomes 0.

# Continue until the queue becomes empty.

# Return true if completed == numCourses; otherwise, return false.

from typing import List
from collections import deque

class Solution:
    # Checks if all courses can be finished using Kahn's Algorithm.
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # Build graph and indegree from prerequisites.
        for pairValue in prerequisites:
            course = pairValue[0]
            prerequisite = pairValue[1]

            adj[prerequisite].append(course)
            indegree[course] += 1

        q = deque()

        # Add courses with no prerequisites.
        for course in range(numCourses):
            # Zero indegree means this course can be completed now.
            if indegree[course] == 0:
                q.append(course)

        completed = 0

        # Complete courses in prerequisite-safe order.
        while q:
            course = q.popleft()

            # Count the current course as completed.
            completed += 1

            # Remove current course as prerequisite for dependent courses.
            for nextCourse in adj[course]:
                indegree[nextCourse] -= 1

                # If all prerequisites are done, add this course.
                if indegree[nextCourse] == 0:
                    q.append(nextCourse)

        # All courses are possible only when all get completed.
        return completed == numCourses


# Driver code.
if __name__ == "__main__":
    numCourses = 2

    prerequisites = [
        [1, 0],
        [0, 1]
    ]

    sol = Solution()

    print(str(sol.canFinish(numCourses, prerequisites)).lower())
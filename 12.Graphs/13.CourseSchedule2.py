# Given numCourses courses labeled from 0 to numCourses - 1 and a list of prerequisite pairs, return any valid order for completing all courses.

# Each pair [course, prerequisite] means the prerequisite course must be completed before the course. Return an empty array when no valid order exists due to circular dependency.

# Example 1
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]

# Output: [0,1,2,3]

# Explanation: Course 0 appears before courses 1 and 2, and both appear before course 3.

# Example 2
# Input: numCourses = 3, prerequisites = [[0,1],[1,2],[2,0]]

# Output: []

# Explanation: The courses form a circular dependency, so no valid ordering exists.

# Approach 1
# Every course represents a vertex, while each prerequisite pair creates a directed edge from the prerequisite course to the dependent course. DFS appends a course only after all dependent paths have been explored, producing a postorder that becomes a valid course order after reversal.

# A three-state array distinguishes unvisited, active, and finished courses. Reaching an active course indicates a circular dependency, making completion of all courses impossible.

# Algorithm
# Build an adjacency list containing an edge from every prerequisite to the corresponding dependent course.

# Initialize a state array with 0 for unvisited courses and create an empty postorder list.

# Traverse every course and start DFS from each unvisited course, ensuring coverage of disconnected dependency chains.

# Mark the current course with state 1, indicating membership in the active DFS path.

# Examine every dependent course; return an empty array upon reaching state 1, and continue DFS recursively upon reaching state 0.

# Mark the current course with state 2 after all dependent paths finish and append the course to the postorder list.

# Reverse the postorder list and return the result when no cycle is detected, placing every prerequisite before the corresponding dependent course.

from typing import List

class Solution:
    # Function to return a valid course order.
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]

        # Build edge from prerequisite to dependent course.
        for course, prerequisite in prerequisites:
            adj[prerequisite].append(course)

        state = [0] * numCourses
        order: List[int] = []

        # Function to build order after prerequisite paths finish.
        def dfs(course: int) -> bool:
            # State 1 means course is active in current path.
            if state[course] == 1:
                return False

            # State 2 means course is already placed safely.
            if state[course] == 2:
                return True

            state[course] = 1

            # Visit all courses depending on current course.
            for next_course in adj[course]:
                if not dfs(next_course):
                    return False

            # Mark course finished and place in postorder.
            state[course] = 2
            order.append(course)
            return True

        # Start DFS from every unvisited course.
        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(course):
                    return []

        # Reverse postorder to place prerequisites first.
        order.reverse()
        return order

# Driver code.
def main() -> None:
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

    sol = Solution()
    print(sol.findOrder(numCourses, prerequisites))

if __name__ == "__main__":
    main()

# Approach 2
# Kahn’s Algorithm begins with all courses having indegree 0, since such courses have no pending prerequisites. Every removed course is appended directly to the resulting course order.

# Processing a course reduces the indegree of all dependent courses. A dependent course enters the queue only after all prerequisites have been processed. An incomplete final order indicates a cycle.

# Algorithm
# Build an adjacency list and indegree array from all prerequisite pairs, storing the dependency graph and incoming-edge count of every course.

# Add every course having indegree 0 to a queue, since such courses can be completed immediately.

# Initialize an empty order list to store courses in valid prerequisite order.

# Continue processing while the queue contains courses, removing the front course and appending the course to the order.

# Reduce the indegree of every dependent course, representing the completion of one required prerequisite.

# Add a dependent course to the queue when the indegree becomes 0, indicating that all prerequisites have been completed.

# Return the order when the list contains V courses; otherwise, return an empty array because a cycle prevents completion.

# Note: Multiple valid course orders can exist. DFS and Kahn’s Algorithm may return different orders, but every order is correct when each prerequisite appears before the corresponding dependent course.
# A cycle makes course completion impossible: DFS detects an active-path vertex, while Kahn’s Algorithm processes fewer than V courses. Both approaches return an empty array when a cycle exists.

from collections import deque
from typing import Deque, List

class Solution:
    # Function to return a valid course order.
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        # Build graph and indegree from prerequisites.
        for course, prerequisite in prerequisites:
            adj[prerequisite].append(course)
            indegree[course] += 1

        queue: Deque[int] = deque()

        # Add courses with no prerequisites.
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        order: List[int] = []

        # Process courses in prerequisite-safe order.
        while queue:
            course = queue.popleft()
            order.append(course)

            # Remove current course as prerequisite for dependent courses.
            for next_course in adj[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0:
                    queue.append(next_course)

        # Cycle exists when not all courses are processed.
        if len(order) != numCourses:
            return []

        return order

# Driver code.
def main() -> None:
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

    sol = Solution()
    print(sol.findOrder(numCourses, prerequisites))

if __name__ == "__main__":
    main()

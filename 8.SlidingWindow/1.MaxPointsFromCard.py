# Given an integer array cardPoints and an integer k, you have to pick exactly k cards.

# In one move, you can pick a card either from the beginning or from the end of the array.

# Return the maximum score you can obtain after picking exactly k cards.

# Example 1
# Input: cardPoints = [1, 2, 3, 4, 5, 6, 1], k = 3

# Output: 12

# Explanation: We can pick 6 and 1 from the end, and 5 from the end before them. The selected cards are 5, 6, and 1. Their total score is 12.

# Example 2
# Input: cardPoints = [2, 2, 2], k = 2

# Output: 4

# Explanation: Any two cards can be picked, and the maximum score will be 4.

# Brute Force Approach
# Every valid selection contains some cards from the left end and the remaining cards from the right end. For k selections, the number of left cards can range from 0 to k.

# Each possible split can be evaluated independently by recalculating the corresponding left and right sums. Complete split examination guarantees the maximum score, but repeated summation increases the running time.

# Algorithm
# Store the array size in n and return -1 when k < 0 or k > n.

# Return 0 when k equals 0, and return the total array sum when k equals n.

# Initialize maxScore with the smallest possible value to support negative card values.

# Traverse leftCount from 0 to k and calculate rightCount = k - leftCount.

# Add the first leftCount values and the final rightCount values to obtain currentScore.

# Update maxScore with the larger value between maxScore and currentScore, then return maxScore after checking every split.

class Solution:

    # Finds the maximum score by evaluating every left-right split.
    def max_score(self, card_points: list[int], k: int) -> int:
        n = len(card_points)

        # Invalid k cannot form a valid selection.
        if k < 0 or k > n:
            return -1

        # Picking no cards gives a score of zero.
        if k == 0:
            return 0

        # Picking all cards requires the complete array sum.
        if k == n:
            return sum(card_points)

        max_score = float("-inf")

        # Try every possible number of cards taken from the left.
        for left_count in range(k + 1):
            right_count = k - left_count
            current_score = 0

            # Add the selected cards from the left end.
            for i in range(left_count):
                current_score += card_points[i]

            # Add the remaining selected cards from the right end.
            for i in range(right_count):
                current_score += card_points[n - 1 - i]

            # Keep the best score among all valid splits.
            if current_score > max_score:
                max_score = current_score

        return int(max_score)


if __name__ == "__main__":
    card_points = [1, 2, 3, 4, 5, 6, 1]
    k = 3

    solution = Solution()

    print(solution.max_score(card_points, k))

# Complexity Analysis
# Time Complexity: O(K²), because K + 1 splits receive examination and up to K selected values may require summation for every split.

# Space Complexity: O(1), because only counters and sum variables require auxiliary storage.

# Better Approach
# Repeated summation can be removed by precomputing scores for every possible number of cards selected from each end.

# Array leftSum stores sums of the first i cards, while rightSum stores sums of the final i cards. Any split score can then be obtained in constant time by combining one prefix value and one suffix value.

# Algorithm
# Store the array size in n and return -1 when k < 0 or k > n.

# Return 0 when k equals 0, and return the total array sum when k equals n.

# Create leftSum and rightSum with size k + 1, with position 0 initialized to 0.

# Build leftSum[i] using the first i cards and rightSum[i] using the final i cards.

# Traverse leftCount from 0 to k, calculate rightCount = k - leftCount, and obtain currentScore = leftSum[leftCount] + rightSum[rightCount].

# Update maxScore for every split and return maxScore after complete traversal.

class Solution:

    # Finds the maximum score using precomputed left and right sums.
    def max_score(self, card_points: list[int], k: int) -> int:
        n = len(card_points)

        # Invalid k cannot form a valid selection.
        if k < 0 or k > n:
            return -1

        # Picking no cards gives a score of zero.
        if k == 0:
            return 0

        # Picking all cards requires the complete array sum.
        if k == n:
            return sum(card_points)

        left_sum = [0] * (k + 1)
        right_sum = [0] * (k + 1)

        # Store sums for every possible number of left cards.
        for i in range(1, k + 1):
            left_sum[i] = (
                left_sum[i - 1] + card_points[i - 1]
            )

        # Store sums for every possible number of right cards.
        for i in range(1, k + 1):
            right_sum[i] = (
                right_sum[i - 1] + card_points[n - i]
            )

        max_score = float("-inf")

        # Combine each valid left count with its matching right count.
        for left_count in range(k + 1):
            right_count = k - left_count

            current_score = (
                left_sum[left_count]
                + right_sum[right_count]
            )

            # Keep the maximum score among all possible splits.
            if current_score > max_score:
                max_score = current_score

        return int(max_score)


if __name__ == "__main__":
    card_points = [1, 2, 3, 4, 5, 6, 1]
    k = 3

    solution = Solution()

    print(solution.max_score(card_points, k))

# Complexity Analysis
# Time Complexity: O(K), because construction of both sum arrays and examination of all K + 1 splits require linear time.

# Space Complexity: O(K), because leftSum and rightSum each contain K + 1 values.

# Optimal Approach
# Selecting the first k cards forms one valid split. Replacing one selected left card with one card from the right creates the next possible split.

# Every replacement removes the rightmost card from the current left selection and adds the next available card from the right end. Repeating the replacement k times generates all possible left-right distributions without extra arrays.

# Algorithm
# Store the array size in n and return -1 when k < 0 or k > n.

# Return 0 when k equals 0, and return the total array sum when k equals n.

# Calculate the sum of the first k cards and store the result in currentScore.

# Initialize maxScore with currentScore and rightIndex with n - 1.

# Traverse leftIndex from k - 1 down to 0. During each step, subtract cardPoints[leftIndex] because that card leaves the left selection, add cardPoints[rightIndex] because the next card from the right enters the selection, then decrement rightIndex.

# Update maxScore after every replacement, then return maxScore after generating all possible splits.

class Solution:

    # Finds the maximum score by shifting selections between both ends.
    def max_score(self, card_points: list[int], k: int) -> int:
        n = len(card_points)

        # Invalid k cannot form a valid selection.
        if k < 0 or k > n:
            return -1

        # Picking no cards gives a score of zero.
        if k == 0:
            return 0

        # Picking all cards requires the complete array sum.
        if k == n:
            return sum(card_points)

        current_score = 0

        # Start with all k selected cards taken from the left.
        for i in range(k):
            current_score += card_points[i]

        max_score = current_score
        right_index = n - 1

        # Replace one left card with one right card in each step.
        for left_index in range(k - 1, -1, -1):
            current_score -= card_points[left_index]
            current_score += card_points[right_index]
            right_index -= 1

            # Keep the best score after each new split.
            if current_score > max_score:
                max_score = current_score

        return max_score


if __name__ == "__main__":
    card_points = [1, 2, 3, 4, 5, 6, 1]
    k = 3

    solution = Solution()

    print(solution.max_score(card_points, k))
# An integer array asteroids is given. Each value represents one asteroid in a row. The absolute value represents size, a positive value means movement toward the right, and a negative value means movement toward the left.

# All asteroids move at the same speed. When two asteroids meet, the smaller asteroid explodes, and the larger asteroid keeps moving in the same direction. When sizes are equal, both asteroids explode. Asteroids moving in the same direction never meet. Return the final state after all collisions.

# Example 1
# Input: asteroids = [5, 10, -5]
# Output: [5, 10]
# Explanation: Asteroid 10 destroys asteroid -5 and keeps moving right. Asteroid 5 and asteroid 10 move in the same direction, so no collision happens.

# Approach
# A new left-moving asteroid first collides with the nearest earlier right-moving asteroid. If that asteroid explodes, the next nearest right-moving asteroid is checked. Therefore, the most recently stored asteroid must be processed first, which follows the LIFO order of a stack.

# Asteroids moving away from each other never collide, so only earlier right-moving asteroids need to be checked. An array-based stack works well because adding, checking, and removing the last asteroid are fast, and the final remaining asteroids can easily be returned as an array.

# Algorithm
# Begin with an empty array named survivors so stack operations and final answer storage use the same simple structure.

# Move through asteroids from left to right because only already-seen asteroids can stand in front of the current asteroid.

# Store every right-moving asteroid directly, because earlier asteroids cannot move toward a new right-moving asteroid.

# Treat every left-moving asteroid as an incoming challenger, and keep the absolute size so comparisons use size instead of direction sign.

# Remove smaller right-moving asteroids from the end of survivors, because each smaller asteroid explodes before the incoming asteroid can move farther left.

# Stop the collision chain if an equal or larger right-moving asteroid is found, because equal size removes both asteroids and larger size destroys the incoming asteroid.

# Store the left-moving asteroid after all blockers disappear, so the final answer retains the surviving left mover.

# Return survivors because the array keeps all remaining asteroids in left-to-right order.

from typing import List


class Solution:
    # Simulates asteroid collisions with an array stack.
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        survivors: List[int] = []

        # Process asteroids from left to right.
        for asteroid in asteroids:
            # A right mover cannot hit earlier asteroids.
            if asteroid > 0:
                survivors.append(asteroid)
            else:
                current_size = abs(asteroid)
                destroyed = False

                # Check only right movers nearest to the asteroid.
                while survivors and survivors[-1] > 0:
                    top_size = abs(survivors[-1])

                    # Smaller right movers explode first.
                    if top_size < current_size:
                        survivors.pop()
                    else:
                        # Equal size removes the stored asteroid too.
                        if top_size == current_size:
                            survivors.pop()

                        destroyed = True
                        break

                # Store a left mover after every blocker is gone.
                if not destroyed:
                    survivors.append(asteroid)

        return survivors


# Driver code
def main() -> None:
    asteroids = [10, 2, -5]
    obj = Solution()
    answer = obj.asteroidCollision(asteroids)
    print(answer)


if __name__ == "__main__":
    main()
# Given two sorted integer arrays nums1 and nums2, merge both the arrays into a single array sorted in non-decreasing order.
# The final sorted array should be stored inside the array nums1 and it should be done in-place.
# Array nums1 has a length of m + n, where the first m elements denote the elements of nums1 and rest are 0s whereas nums2 has a length of n.

# solution
# We are given two sorted arrays nums1 and nums2 and nums1 has enough space at the end (filled with zeros) to accommodate all elements from nums2. Now, if we try to insert elements from nums2 into nums1 from the beginning, we would need to shift elements in nums1 every time to make room which becomes time consuming and inefficient.
# Since both arrays are sorted in non-decreasing order, the largest elements will be at the end of each array. If we start comparing elements from the back of both arrays and place the largest one at the end of nums1, we won't need to shift anything.
# To efficiently insert elements at the end, we will use three pointers.
# Initialize three pointers: One points at the last valid index (excluding zeros) of nums1, one points at the last valid index of nums2 andd the last pointer points to last index of nums1.
# Compare the elements pointed by the first two pointers and whichever is larger, place it at the third pointer's index.
# Move the respective pointer one step back and also move the third pointer one step back.
# If there are any remaining elements in nums2, then copy them in nums1. If any elements remain in nums1, they’re already in place
# The result is a fully merged and sorted array stored in nums1 itself.

class Solution:
    # Merges nums2 into nums1 in-place in sorted order.
    def merge(self, nums1, m, nums2, n):
        # i: last valid element index in nums1
        i = m - 1

        # j: last index of nums2
        j = n - 1

        # k: end of nums1 array
        k = m + n - 1

        # Merge from the back to avoid overwriting
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If any elements remain in nums2, copy them
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1

        # No need to copy nums1 leftovers — already in place

# Example usage
nums1 = [1, 3, 5, 0, 0, 0]
nums2 = [2, 4, 6]
m, n = 3, 3
Solution().merge(nums1, m, nums2, n)
print(nums1)

# Time Complexity: O(N+M), we traverse both the arrays exactly once.
# Space Complexity: O(1), constant extra space is used to store pointers.
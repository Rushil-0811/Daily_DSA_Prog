# You are given a sorted array arr of distinct values and a target value x. You need to search for the index of the target value in the array
class BinarySearchInsert:
    def search_insert(self, arr, x):
        n = len(arr)
        low, high = 0, n - 1
        ans = n  # Default if x is larger than all elements

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] >= x:
                ans = mid  # Potential answer, look on left side
                high = mid - 1
            else:
                low = mid + 1  # Look on right side

        return ans

# Main execution
if __name__ == "__main__":
    arr = [1, 2, 4, 7]
    x = 6
    obj = BinarySearchInsert()
    index = obj.search_insert(arr, x)
    print(f"The index is: {index}")

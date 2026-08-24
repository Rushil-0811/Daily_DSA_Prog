#  Given an array ‘arr of integer numbers, ‘ar[i]’ represents the number of pages in the ‘i-th’ book. There are a ‘m’ number of students, and the task is to allocate all the books to the students.
# Allocate books in such a way that:

# Each student gets at least one book.
# Each book should be allocated to only one student.
# Book allocation should be in a contiguous manner.
# You have to allocate the book to ‘m’ students such that the maximum number of pages assigned to a student is minimum. If the allocation of books is not possible. return -1

# Example 1:

# Input Format: n = 4, m = 2, arr[] = {12, 34, 67, 90}
# Result: 113
# Explanation: The allocation of books will be 12, 34, 67 | 90. One student will get the first 3 books and the other will get the last one.

# brute
# If m > n: In this case, book allocation is not possible and so, we will return -1.
# Next, we will find the maximum element and the summation of the given array.
# We will use a loop(say pages) to check all possible pages from max(arr[]) to sum(arr[]).
# Next, inside the loop, we will send each ‘pages’, to the function countStudents() function to get the number of students to whom we can allocate the books.
# The first number of pages, ‘pages’, for which the number of students will be equal to ‘m’, will be our answer. So, we will return that particular ‘pages’.
# Finally, if we are out of the loop, we will return max(arr[]) as there cannot exist any answer smaller than that.

def countStudents(arr, pages):
    n = len(arr)  # size of array
    students = 1
    pagesStudent = 0
    for i in range(n):
        if pagesStudent + arr[i] <= pages:
            # add pages to current student
            pagesStudent += arr[i]
        else:
            # add pages to next student
            students += 1
            pagesStudent = arr[i]
    return students

def findPages(arr, n, m):
    # book allocation impossible
    if m > n:
        return -1

    low = max(arr)
    high = sum(arr)

    for pages in range(low, high + 1):
        if countStudents(arr, pages) == m:
            return pages
    return low

arr = [25, 46, 28, 49, 24]
n = 5
m = 4
ans = findPages(arr, n, m)
print("The answer is:", ans)

# Time Complexity: O(N * (sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, max(arr[])

# Space Complexity:  O(1) as we are not using any extra space to solve this problem.

# optimal
# This problem is solved using Binary Search to efficiently find the best way to distribute books among students.
# The main idea is to cut the search range in half each time by checking whether a certain number of pages per student is possible or not.
# The possible range of answers lies between the largest book (since no student can receive less than the largest book) and the total number of pages (which means giving all books to one student).
# First, if there are more students than books, it's impossible to assign at least one book to each student, so we return -1.
# Next, we search between the minimum and maximum possible values:
# The minimum possible is the largest single book (because every student must get at least one complete book).
# The maximum possible is the sum of all pages (if one student reads all books).
# We perform Binary Search:
# We try a middle value of pages per student.
# We check how many students would be required if no student gets more than that value.
# If it takes more students than allowed, that value is too low, so we try a higher one.
# If it fits within the allowed number of students, we store it and try a smaller one to find an even better option.
# Eventually, we land on the smallest value that works this is our answer.
# Note: After the binary search loop ends, the pointer will be on the smallest possible maximum number of pages per student. That's why it gives the correct result directly.

def countStudents(arr, pages):
    n = len(arr)  # size of array
    students = 1
    pagesStudent = 0
    for i in range(n):
        if pagesStudent + arr[i] <= pages:
            # add pages to current student
            pagesStudent += arr[i]
        else:
            # add pages to next student
            students += 1
            pagesStudent = arr[i]
    return students

def findPages(arr, n, m):
    # book allocation impossible
    if m > n:
        return -1

    low = max(arr)
    high = sum(arr)
    while low <= high:
        mid = (low + high) // 2
        students = countStudents(arr, mid)
        if students > m:
            low = mid + 1  
        else:
            high = mid - 1  
    return low

arr = [25, 46, 28, 49, 24]
n = 5
m = 4
ans = findPages(arr, n, m)
print("The answer is:", ans)

# Time Complexity: O(N * log(sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, max(arr[]) = maximum of all array elements.

# Space Complexity:  O(1) as we are not using any extra space to solve this problem.

import time

# Merge Sort Function
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursive calls
        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        # Merge the two halves
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Copy remaining elements of left[]
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        # Copy remaining elements of right[]
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# User Input
n = int(input("Enter the number of elements: "))
arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Start Execution Time
start = time.perf_counter()

# Perform Merge Sort
merge_sort(arr)

# End Execution Time
end = time.perf_counter()

# Display Sorted Array
print("\nSorted Array:")
for i in range(n):
    print(arr[i], end=" ")

# Display Execution Time
print("\n\nExecution Time:", end - start, "seconds")

# Display Time Complexity
print("\nTime Complexity:")
print("Best Case    : O(n log n)")
print("Average Case : O(n log n)")
print("Worst Case   : O(n log n)")
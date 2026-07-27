import time

# Quick Sort Function
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

# Partition Function
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp

    temp = arr[i + 1]
    arr[i + 1] = arr[high]
    arr[high] = temp

    return i + 1

# User Input
n = int(input("Enter the number of elements: "))
arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Start Execution Time
start = time.perf_counter()

# Perform Quick Sort
quick_sort(arr, 0, n - 1)

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
print("Worst Case   : O(n²)")

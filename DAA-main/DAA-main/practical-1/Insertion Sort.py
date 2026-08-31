import time

# User Input
n = int(input("Enter the number of elements: "))
arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Start Execution Time
start = time.perf_counter()

# Insertion Sort
for i in range(1, n):
    key = arr[i]
    j = i - 1

    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j + 1] = key

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
print("Best Case    : O(n)")
print("Average Case : O(n²)")
print("Worst Case   : O(n²)")

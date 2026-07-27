import time

# User Input
n = int(input("Enter the number of elements: "))
arr = []

print("Enter the elements:")
for i in range(n):
    arr.append(int(input()))

# Start Execution Time
start = time.perf_counter()

# Selection Sort
for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if arr[j] < arr[min_index]:
            min_index = j

    # Swap elements
    temp = arr[i]
    arr[i] = arr[min_index]
    arr[min_index] = temp

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
print("Best Case    : O(n²)")
print("Average Case : O(n²)")
print("Worst Case   : O(n²)")

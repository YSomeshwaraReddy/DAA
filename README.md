                                         1. Bubble Sort
 Summary:
 Bubble Sort repeatedly compares adjacent elements and swaps them if they are in the wrong order. After each pass, the largest unsorted element "bubbles" to its correct position. It is simple to implement but inefficient for large datasets.

Conclusion:
Bubble Sort is an easy-to-understand sorting algorithm suitable for learning basic sorting concepts. However, due to its high time complexity of O(n²), it is not recommended for large datasets.


                                         2. Selection Sort
Summary:
Selection Sort works by repeatedly finding the smallest element from the unsorted portion of the array and placing it at the beginning. This process continues until the entire array is sorted.

Conclusion:
Selection Sort performs fewer swaps compared to Bubble Sort, but its time complexity remains O(n²). It is useful for educational purposes and small datasets but is not efficient for large-scale applications.


                                          3. Insertion Sort
 Summary:
 Insertion Sort builds the sorted array one element at a time by inserting each element into its correct position among the previously sorted elements. It is efficient for small and nearly sorted datasets.

Conclusion:
Insertion Sort is simple, stable, and performs well on small or partially sorted data. Although its worst-case time complexity is O(n²), it can outperform other simple sorting 
algorithms in practical situations involving small datasets.


                                          4. Merge Sort
 Summary:
 Merge Sort follows the Divide-and-Conquer approach. It divides the array into smaller subarrays, recursively sorts them, and then merges them back together in sorted order.

Conclusion:
Merge Sort is a highly efficient and stable sorting algorithm with a time complexity of O(n log n). It is suitable for large datasets and applications requiring consistent performance, though it requires additional memory for merging.


                                           5. Quick Sort
Summary:
Quick Sort also uses the Divide-and-Conquer strategy. It selects a pivot element, partitions the array into smaller and larger elements relative to the pivot, and recursively sorts the partitions.

Conclusion:
Quick Sort is one of the fastest sorting algorithms in practice, with an average time complexity of O(n log n). It is widely used due to its efficiency and low memory usage, although its worst-case complexity can reach O(n²) if the pivot is chosen poorly.

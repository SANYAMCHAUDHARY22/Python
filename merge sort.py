
import random
import time

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

if __name__ == "__main__":
    arr = [random.randint(0, 100) for _ in range(10)]
    print(f"Original array: {arr}")
    start = time.time()
    merge_sort(arr)
    print(f"Sorted array: {arr}")
    print(f"Time taken: {time.time() - start}")

# The merge sort algorithm is a divide-and-conquer algorithm that divides the input array into two halves, recursively sorts the two halves, and then merges the sorted halves to produce a sorted array. The time complexity of the merge sort algorithm is O(n log n), where n is the number of elements in the array. This means that the time taken to sort an array is proportional to the number of elements in the array multiplied by the logarithm of the number of elements. The merge sort algorithm is efficient for large arrays and has a stable time complexity, making it a popular choice for sorting large datasets.
# The merge sort algorithm can be implemented in Python using a recursive approach. The merge_sort function takes an array arr as input and recursively divides the array into two halves. It then sorts the two halves using the merge_sort function and merges the sorted halves to produce a sorted array. The main function generates a random array of 10 elements and prints the original array. It measures the time taken to sort the array using the merge_sort function and prints the sorted array and the time taken.
# The merge sort algorithm is a popular sorting algorithm that is widely used in practice due to its efficiency and stability. It is a good choice for sorting large datasets and is often used as the default sorting algorithm in many programming languages and libraries. The merge sort algorithm is also a good example of a divide-and-conquer algorithm, which is a powerful technique for solving complex problems by breaking them down into smaller, more manageable subproblems.
# write code for heap sort
# write code for bubble sort
# write code for insertion sort
    
    
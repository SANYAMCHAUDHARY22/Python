#write quick sort algorithm

import random
import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    arr = [random.randint(0, 100) for _ in range(10)]
    print(f"Original array: {arr}")
    start = time.time()
    print(f"Sorted array: {quick_sort(arr)}")
    print(f"Time taken: {time.time() - start}")


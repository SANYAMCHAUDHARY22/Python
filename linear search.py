#write code for linear search
import random
import time
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:

            return i
    return -1
if __name__ == "__main__":
    arr = [random.randint(0, 100) for _ in range(10)]
    print(f"Original array: {arr}")
    x = random.choice(arr)
    print(f"Element to be searched: {x}")
    start = time.time()
    print(f"Index of {x}: {linear_search(arr, x)}")
    print(f"Time taken: {time.time() - start}")
# The linear search algorithm is a simple algorithm that searches for a given element in an array. It iterates through the array and compares each element with the given element. If the element is found, it returns the index of the element; otherwise, it returns -1. The time complexity of the linear search algorithm is O(n), where n is the number of elements in the array. This means that the time taken to search for an element in the array is directly proportional to the number of elements in the array. The linear search algorithm is not very efficient for large arrays, as it has to iterate through each element in the array. However, it is a simple and easy-to-understand algorithm that can be used for small arrays or when the array is not sorted.
#
# The linear search algorithm can be implemented in Python using a simple for loop. The linear_search function takes an array arr and an element x as input and iterates through the array using a for loop. It compares each element in the array with the given element x and returns the index of the element if it is found. If the element is not found, it returns -1. The main function generates a random array of 10 elements and prints the original array. It then selects a random element from the array and prints the element to be searched. It measures the time taken to search for the element using the linear_search function and prints the index of the element and the time taken.

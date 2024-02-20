#bubble sort

import random
import time 
 
def bubble_sort(arr):
    


    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr




if __name__ == "__main__":
    arr = [random.randint(0, 100) for i in range(10)]



    print(arr)
    print(bubble_sort(arr)) 
    print(arr)  

    arr = [random.randint(0, 100) for i in range(100)]
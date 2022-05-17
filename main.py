import time
import sys
from numpy import random

sys.setrecursionlimit(3000)

n = 500000

array = random.randint(1, 300, n)
array2 = random.randint(1, 300, n)
array3 = random.randint(1, 300, n)
array4 = random.randint(1, 300, n)


# quick sort
def partition(array, p, r):
    x = array[r]
    i = p - 1
    j = p
    for j in range(p, r):
        if array[j] <= x:
            i += 1
            array[j], array[i] = array[i], array[j]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


def quick_sort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quick_sort(array, p, q - 1)
        quick_sort(array, q + 1, r)


# merge sort

def merge_sort(A):
    if len(A) > 1:
        mid = len(A) // 2

        left = A[:mid]
        right = A[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1


# heapsort
def heap_sort(A):
    for i in range(n // 2 - 1, -1, -1):
        heapif(A, i, n)
    for i in range(n - 1, -1, -1):
        heapif(A, 0, i)
        heapif(A, 0, i)
        A[0], A[i] = A[i], A[0]


def heapif(A, idx, max):
    left = 2 * idx + 1
    right = 2 * idx + 2
    if (left < max and A[left] > A[idx]):
        largest = left
    else:
        largest = idx
    if (right < max and A[right] > A[largest]):
        largest = right
    if (largest != idx):
        A[idx], A[largest] = A[largest], A[idx]
        heapif(A, largest, max)


# my own algorithms sort
# bubble sort

def bubbleSort(array):
    for i in range(len(array) - 1):
        for j in range(0, len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]





def main():
    print("Here we go Luigi 😂🤣, and [*] for my PC\n")
    print("=======================================\n")

    before_sort = array
    print(f"Before sort: {before_sort}\n")
    start_time_tree = time.time()
    bubbleSort(array)
    print(f"After sort with bubble sort: {array} \n")
    print(f"{time.time() - start_time_tree} seconds with binary bubble sort\n")

    before_sort = array2
    print(f"Before sort: {before_sort}\n")
    start_time = time.time()
    quick_sort(array2, 0, len(array2) - 1)
    print(f"After sort: {array2}\n")
    print(f"{time.time() - start_time} seconds with quick sort\n")
    print("=======================================\n")

    before_sort = array3
    print(f"Before sort: {before_sort}\n")
    start_time_2 = time.time()
    merge_sort(array3)
    print(f"After sort: {array3}\n")
    print(f"{time.time() - start_time_2} seconds with merge sort\n")
    print("=======================================\n")

    before_sort = array4
    print(f"Before sort: {before_sort}\n")
    start_time_3 = time.time()
    heap_sort(array4)
    print(f"After sort: {array4}\n")
    print(f"{time.time() - start_time_3} seconds with heap sort\n")


main()
